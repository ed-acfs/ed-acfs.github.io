"""Sincronizza con Spansh sia la tabella sistemi in about/index.md sia i
dati della mappa 3D in map/json_files/sistemi.json, in un'unica esecuzione,
cosi che le due fonti non si disallineino piu' fra un aggiornamento e
l'altro. Aggiorna Governo, Popolazione, Alleanza e Stato dei sistemi nella
tabella; coordinate, stato Controllato/Non Controllato e categorie
Material Trader/Technology Broker/Interstellar Factor nella mappa.

Esecuzione ancora manuale (nessuno scheduling automatico e' stato deciso):
    python spansh_sync.py

Usa l'API pubblica (non ufficiale) di Spansh, non richiede API key.
https://github.com/EDCD/EDDI/issues/2327 documenta gli endpoint.
"""

import json
import re
from datetime import date

import requests

SEARCH_URL = "https://spansh.co.uk/api/systems/search"
STATIONS_URL = "https://spansh.co.uk/api/stations/search"
FACTION_NAME = "Flotta Stellare"
USER_AGENT = "ACFS-website-bot/1.0 (+https://ed-acfs.github.io)"

ABOUT_PATH = "about/index.md"
MAP_PATH = "map/json_files/sistemi.json"

# Traduzioni verso l'italiano usate nel resto della tabella (ricavate dalle
# righe già presenti nel file, non dalla traduzione ufficiale del gioco).
GOVERNMENT_IT = {
    "Democracy": "Democratico",
    "Corporate": "Corporativo",
    "Confederacy": "Confederato",
    "Anarchy": "Anarchico",
    "Dictatorship": "Dittatoriale",
    "Theocracy": "Teocratico",
    "Cooperative": "Cooperativo",
    "Patronage": "Patronale",
    "Feudal": "Feudale",
    "None": "Nessuno",
}
ALLEGIANCE_IT = {
    "Federation": "Federale",
    "Empire": "Imperiale",
    "Independent": "Indipendente",
}

# Nomi noti come errati nel file: nome scritto -> nome reale su Spansh.
NAME_FIXES = {
    "V0502 V0502 Ophiuchii": "V0502 Ophiuchii",
}

# Categorie della mappa (map/json_files/sistemi.json -> categories."Sistemi
# della Flotta"/"Material Traders"/"Punti di Interesse"): id numerico fisso,
# non derivabile dal JSON stesso perché va assegnato ai sistemi.
CAT_CONTROLLATO = 1
CAT_NON_CONTROLLATO = 2
CAT_STATUS_IDS = {0, 1, 2}  # 0 = Capitale, mai riassegnato da qui
MATERIAL_TRADER_CAT = {"Raw": 3, "Manufactured": 4, "Encoded": 5}
TECH_BROKER_CAT = {"Human": 7, "Guardian": 8}
INTERSTELLAR_FACTOR_CAT = 6
CAT_EXTRA_IDS = {3, 4, 5, 6, 7, 8}


# ---------------------------------------------------------------------------
# Fetch condiviso da Spansh
# ---------------------------------------------------------------------------

def fetch_all_presence_systems():
    """Scarica, paginando, tutti i sistemi in cui Flotta Stellare ha presenza."""
    systems = []
    page = 0
    while True:
        response = requests.post(
            SEARCH_URL,
            json={
                "filters": {"minor_faction_presences": {"value": [FACTION_NAME]}},
                "sort": [{"name": {"direction": "asc"}}],
                "size": 100,
                "page": page,
            },
            headers={"User-Agent": USER_AGENT},
        )
        response.raise_for_status()
        data = response.json()
        systems.extend(data["results"])
        if len(systems) >= data["count"]:
            break
        page += 1
    return systems


def fetch_stations_for_systems(names, chunk_size=40):
    """Scarica tutte le stazioni dei sistemi indicati (serve per Material
    Trader/Technology Broker/Interstellar Factor sulla mappa). Il filtro
    ``system_name`` accetta piu' nomi insieme, quindi si procede a blocchi
    per contenere il numero di richieste."""
    stations = []
    for i in range(0, len(names), chunk_size):
        chunk = names[i:i + chunk_size]
        page = 0
        while True:
            response = requests.post(
                STATIONS_URL,
                json={"filters": {"system_name": {"value": chunk}}, "size": 100, "page": page},
                headers={"User-Agent": USER_AGENT},
            )
            response.raise_for_status()
            data = response.json()
            stations.extend(data["results"])
            if (page + 1) * 100 >= data["count"]:
                break
            page += 1
    return stations


# ---------------------------------------------------------------------------
# Sync about/index.md
# ---------------------------------------------------------------------------

def format_population(pop):
    """Formatta il valore numerico **esattamente** come mostra EDSM/Spansh.

    Si limita ad applicare il separatore delle migliaia con il punto. Evita
    suffissi "milioni"/"miliardi" perché la richiesta dell'utente è di usare
    lo stesso formato che si vede sul sito (es. 14 Geminorum → ``36.586.522``).
    """
    if pop is None:
        return ""
    if pop == 0:
        return "0"
    return f"{int(pop):,}".replace(',', '.')


def update_last_modified(content):
    """Aggiorna il campo ``last_modified_at`` nel front matter con la data odierna."""
    return re.sub(
        r'^last_modified_at:\s*\d{4}-\d{2}-\d{2}',
        f'last_modified_at: {date.today().isoformat()}',
        content,
        count=1,
        flags=re.MULTILINE,
    )


def parse_population(value):
    """Converte una popolazione già formattata (``"151.113"``) in intero."""
    if not value:
        return 0
    return int(value.replace('.', ''))


def update_total_population(content, total):
    """Aggiorna la frase "Governiamo su **N** abitanti" con il totale dei
    sistemi Controllato, nello stesso formato (punto) usato nel resto del file."""
    return re.sub(
        r'Governiamo su \*\*[\d.,]+\*\* abitanti',
        f'Governiamo su **{format_population(total)}** abitanti',
        content,
        count=1,
    )


def fields_from_system(system):
    """Ritorna (governo, popolazione, alleanza, stato) in italiano per un
    record restituito da Spansh."""
    government = GOVERNMENT_IT.get(system.get("government"), system.get("government") or "Nessuno")
    allegiance = ALLEGIANCE_IT.get(system.get("allegiance"), "-")
    population = format_population(system.get("population"))
    status = "Controllato" if system.get("controlling_minor_faction") == FACTION_NAME else "Non Controllato"
    return government, population, allegiance, status


def format_row(row, crown_cell):
    crown = crown_cell if row["is_crown"] else "     "
    return (
        f"|{crown}| {row['name']:<28} | {row['government']:<13} | "
        f"{row['population']} | {row['allegiance']:<20} | {row['status']:<16} |\n"
    )


def sync_about(file_path, spansh_systems):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = '<div class="datatable-begin"></div>'
    end_marker = '<div class="datatable-end"></div>'
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    if start_idx == -1 or end_idx == -1:
        print("Marcatori tabella non trovati")
        return

    table_start = start_idx + len(start_marker)
    table_content = content[table_start:end_idx]
    lines = table_content.splitlines(keepends=True)

    header_lines = []
    crown_cell = "     "
    rows = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('| 👑') and 'Sistema' in line:
            header_lines.append(line)  # riga di intestazione con "Sistema"
            continue
        if stripped.startswith('|:-:'):
            header_lines.append(line)  # riga separatore
            continue
        if '|' not in line:
            continue  # righe vuote attorno ai marker, rigenerate a fine funzione
        parts = line.split('|')
        if len(parts) < 7:
            continue
        is_crown = stripped.startswith('| 👑')
        if is_crown:
            crown_cell = parts[1]
        name = parts[2].strip()
        name = NAME_FIXES.get(name, name)
        rows.append({
            "name": name,
            "is_crown": is_crown,
            "government": parts[3].strip(),
            "population": parts[4].strip(),
            "allegiance": parts[5].strip(),
            "status": parts[6].strip(),
        })

    by_name = {r["name"].lower(): r for r in rows}

    spansh_names = {s["name"].lower() for s in spansh_systems}
    field_labels = [
        ("government", "Governo"),
        ("population", "Popolazione"),
        ("allegiance", "Alleanza"),
        ("status", "Stato"),
    ]

    added = 0
    updated = 0
    for system in spansh_systems:
        government, population, allegiance, status = fields_from_system(system)
        new_values = {
            "government": government,
            "population": population,
            "allegiance": allegiance,
            "status": status,
        }
        key = system["name"].lower()
        existing = by_name.get(key)

        if existing is None:
            row = {"name": system["name"], "is_crown": False, **new_values}
            rows.append(row)
            by_name[key] = row
            added += 1
            print(f"  + {system['name']} ({population} ab.)")
            continue

        changes = [
            (label, existing[field], new_values[field])
            for field, label in field_labels
            if existing[field] != new_values[field]
        ]
        if changes:
            for label, old, new in changes:
                print(f"  ~ {existing['name']}: {label} \"{old}\" -> \"{new}\"")
            existing.update(new_values)
            updated += 1

    not_found = [r["name"] for r in rows if r["name"].lower() not in spansh_names]

    rows.sort(key=lambda r: (0 if r["is_crown"] else 1, r["name"].casefold()))

    new_table = ''.join(header_lines[:2])  # riga "Sistema" + riga separatore
    new_table += ''.join(format_row(r, crown_cell) for r in rows)

    new_table = new_table.lstrip("\n")
    new_table = "\n\n" + new_table
    new_table = new_table.rstrip("\n") + "\n\n"

    total_population = sum(
        parse_population(r["population"]) for r in rows if r["status"] == "Controllato"
    )

    updated_content = content[:table_start] + new_table + content[end_idx:]
    updated_content = update_last_modified(updated_content)
    updated_content = update_total_population(updated_content, total_population)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(
        f"\nFatto: {added} sistemi aggiunti, {updated} aggiornati, "
        f"{len(rows) - added - updated} invariati."
    )
    print(f"Popolazione totale sistemi Controllato: {format_population(total_population)}")
    if not_found:
        print(
            f"{len(not_found)} sistemi in tabella non risultano su Spansh "
            f"(lasciati invariati, probabile mancanza di dati recenti nel log di volo): "
            + ", ".join(not_found)
        )


# ---------------------------------------------------------------------------
# Sync map/json_files/sistemi.json
# ---------------------------------------------------------------------------

def _station_service_names(station):
    return {d["name"] if isinstance(d, dict) else d for d in (station.get("services") or [])}


def sync_map(file_path, spansh_systems, stations):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    systems = data["systems"]

    # -- Sistemi + stato Controllato/Non Controllato -----------------------

    flotta_entries = [s for s in systems if isinstance(s["cat"][0], int)]
    other_entries = [s for s in systems if not isinstance(s["cat"][0], int)]  # rotte spedizione (SVN, ecc.)
    by_name = {s["name"].strip().lower(): s for s in flotta_entries}

    added, status_updated = [], []
    for system in spansh_systems:
        key = system["name"].strip().lower()
        desired_status = CAT_CONTROLLATO if system.get("controlling_minor_faction") == FACTION_NAME else CAT_NON_CONTROLLATO
        existing = by_name.get(key)

        if existing is None:
            new_entry = {
                "name": system["name"],
                "coords": {"x": system["x"], "y": system["y"], "z": system["z"]},
                "cat": [desired_status],
            }
            flotta_entries.append(new_entry)
            by_name[key] = new_entry
            added.append(system["name"])
            continue

        cat0 = existing["cat"][0]
        if cat0 == 0:
            continue  # Capitale, mai riassegnato
        if cat0 != desired_status:
            status_updated.append((existing["name"], cat0, desired_status))
            existing["cat"][0] = desired_status

    presence_names = {s["name"].strip().lower() for s in spansh_systems}
    stale = [
        s["name"] for s in flotta_entries
        if s["cat"][0] in (CAT_CONTROLLATO, CAT_NON_CONTROLLATO) and s["name"].strip().lower() not in presence_names
    ]

    # -- Material Trader / Technology Broker / Interstellar Factor ---------

    computed_extra = {}
    for station in stations:
        sysname = station["system_name"]
        cats = computed_extra.setdefault(sysname, set())
        if "Interstellar Factors Contact" in _station_service_names(station):
            cats.add(INTERSTELLAR_FACTOR_CAT)
        tb = station.get("technology_broker")
        if tb in TECH_BROKER_CAT:
            cats.add(TECH_BROKER_CAT[tb])
        mt = station.get("material_trader")
        if mt in MATERIAL_TRADER_CAT:
            cats.add(MATERIAL_TRADER_CAT[mt])

    poi_added, poi_removed = [], []
    for s in flotta_entries:
        base = [c for c in s["cat"] if c in CAT_STATUS_IDS]
        old_extra = sorted(c for c in s["cat"] if c in CAT_EXTRA_IDS)
        new_extra = sorted(computed_extra.get(s["name"], set()))
        if old_extra != new_extra:
            gained = sorted(set(new_extra) - set(old_extra))
            lost = sorted(set(old_extra) - set(new_extra))
            if gained:
                poi_added.append((s["name"], gained))
            if lost:
                poi_removed.append((s["name"], lost))
        s["cat"] = base + new_extra

    # -- Riordina (Capitale, poi alfabetico, poi rotte spedizione) e scrivi --

    capitale = [s for s in flotta_entries if s["cat"][0] == 0]
    rest = [s for s in flotta_entries if s["cat"][0] != 0]
    rest.sort(key=lambda s: s["name"].casefold())
    data["systems"] = capitale + rest + other_entries

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.write("\n")

    cat_label = {3: "Raw", 4: "Manufactured", 5: "Encoded", 6: "Interstellar Factor",
                 7: "Human Tech Broker", 8: "Guardian Tech Broker"}

    print(f"Sistemi aggiunti: {len(added)}")
    for name in added:
        print(f"  + {name}")
    print(f"\nStato Controllato/Non Controllato aggiornato: {len(status_updated)}")
    for name, old, new in status_updated:
        label = {CAT_CONTROLLATO: "Controllato", CAT_NON_CONTROLLATO: "Non Controllato"}
        print(f"  ~ {name}: {label.get(old, old)} -> {label[new]}")
    print(f"\nCategorie Material Trader/Technology Broker/Interstellar Factor aggiunte: {len(poi_added)}")
    for name, cats in poi_added:
        print(f"  + {name}: {[cat_label[c] for c in cats]}")
    if poi_removed:
        print(f"\nCategorie non piu' confermate da Spansh: {len(poi_removed)}")
        for name, cats in poi_removed:
            print(f"  - {name}: {[cat_label[c] for c in cats]}")
    if stale:
        print(
            f"\n{len(stale)} sistemi in mappa non risultano piu' con presenza Flotta Stellare su "
            f"Spansh (lasciati invariati, verificare a mano): " + ", ".join(stale)
        )
    print(f"\nTotale sistemi Flotta nella mappa: {len(capitale) + len(rest)}")


# ---------------------------------------------------------------------------

def main():
    print("Scarico da Spansh tutti i sistemi con presenza di Flotta Stellare...")
    spansh_systems = fetch_all_presence_systems()
    print(f"Trovati {len(spansh_systems)} sistemi su Spansh.")

    print(f"\n== {ABOUT_PATH} ==")
    sync_about(ABOUT_PATH, spansh_systems)

    print(f"\n== {MAP_PATH} ==")
    names = [s["name"] for s in spansh_systems]
    print("Scarico le stazioni dei sistemi (Material Trader/Technology Broker/Interstellar Factor)...")
    stations = fetch_stations_for_systems(names)
    print(f"Trovate {len(stations)} stazioni.")
    sync_map(MAP_PATH, spansh_systems, stations)


if __name__ == "__main__":
    main()
