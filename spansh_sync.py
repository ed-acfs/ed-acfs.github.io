"""Sincronizza la tabella sistemi in about/index.md con lo stato reale di
Flotta Stellare su Spansh: aggiunge i sistemi mancanti e aggiorna Governo,
Popolazione, Alleanza e Stato di quelli già presenti quando i dati sul sito
sono cambiati rispetto al file.

Usa l'API pubblica (non ufficiale) di Spansh, non richiede API key.
https://github.com/EDCD/EDDI/issues/2327 documenta gli endpoint.
"""

import re
from datetime import date

import requests

SEARCH_URL = "https://spansh.co.uk/api/systems/search"
FACTION_NAME = "Flotta Stellare"
USER_AGENT = "ACFS-website-bot/1.0 (+https://ed-acfs.github.io)"

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


def sync(file_path):
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

    print("Scarico da Spansh tutti i sistemi con presenza di Flotta Stellare...")
    spansh_systems = fetch_all_presence_systems()
    print(f"Trovati {len(spansh_systems)} sistemi su Spansh.")

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


if __name__ == "__main__":
    sync("about/index.md")
