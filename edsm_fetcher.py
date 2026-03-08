import requests
import yaml
import os
import re
import time
from urllib.parse import quote

# API key EDSM (opzionale per lettura, ma inclusa se necessaria)
API_KEY = "e4f9cce8851495e529ffa85b95f08b8825deeda9"  # La tua key, ma non usata per lettura base

def fetch_system_population(system_name):
    encoded_name = quote(system_name)
    url = f"https://www.edsm.net/api-v1/systems?systemName={encoded_name}&showInformation=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and len(data) > 0:
            system_data = data[0]
            info = system_data.get('information', {})
            return info.get('population', 0)
        else:
            return None
    else:
        print(f"Errore per {system_name}: {response.status_code}")
        return None

def format_population(pop):
    """Formatta il valore numerico **esattamente** come mostra EDSM.

    Si limita ad applicare il separatore delle migliaia con il punto. Evita
    suffissi "milioni"/"miliardi" perché la richiesta dell'utente è di usare
    lo stesso formato che si vede sul sito (es. 14 Geminorum → ``36.586.522``).
    """
    if pop is None:
        return ""
    if pop == 0:
        return "0"
    # Python usa la virgola per separare le migliaia in ``:,``; convertiamo
    # la virgola in punto per seguire lo stile italiano/EDSM.
    return f"{int(pop):,}".replace(',', '.')


def update_about_table(file_path, max_updates=None):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trova la sezione della tabella delimitata dai marker
    start_marker = '<div class="datatable-begin"></div>'
    end_marker = '<div class="datatable-end"></div>'
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    if start_idx == -1 or end_idx == -1:
        print("Marcatori tabella non trovati")
        return

    table_start = start_idx + len(start_marker)
    table_content = content[table_start:end_idx]

    # Manteniamo i caratteri di fine riga in modo da non alterare alcuna
    # indentazione o spaziatura
    lines = table_content.splitlines(keepends=True)

    updated_lines = []
    update_count = 0
    for line in lines:
        # se non c'è una pipe o è una riga di intestazione/separatore, la lasciamo
        stripped = line.lstrip()
        if '|' not in line or stripped.startswith('| 👑') or stripped.startswith('| Sistema') or re.match(r'^\|\s*[-:]+', stripped):
            updated_lines.append(line)
            continue

        # Estrai il nome del sistema lasciando intatti gli spazi attorno alle pipe
        parts = line.split('|')
        if len(parts) >= 7:
            system_name = parts[2].strip()
            if max_updates is None or update_count < max_updates:
                pop = fetch_system_population(system_name)
                if pop is not None:
                    formatted = format_population(pop)
                    # sostituisco solo il campo popolazione, mantenendo tutte le
                    # pipe e i caratteri di nuova riga originali
                    parts[4] = f" {formatted} "
                    new_line = '|'.join(parts)
                    if line.endswith('\n') and not new_line.endswith('\n'):
                        new_line += '\n'
                    updated_lines.append(new_line)
                    print(f"Aggiornato {system_name}: {formatted}")
                    update_count += 1
                    time.sleep(0.1)
                    continue
        # se non siamo riusciti a processare il sistema, non tocchiamo la riga
        updated_lines.append(line)

    updated_table = ''.join(updated_lines)
    # make sure there is exactly one empty line after the "begin" marker
    # and exactly one empty line before the "end" marker. we strip leading
    # and trailing blank lines and then add the required ones back so the
    # resulting markdown is never broken even if the original file lacked
    # those separatori.
    #
    # After this transformation the fragment will look like:
    # ``\n<first-row>...<last-row>\n\n``
    # which leaves a blank paragraph on both sides when concatenated.
    updated_table = updated_table.lstrip("\n")
    # two newlines: one to move to next line, another blank paragraph
    updated_table = "\n\n" + updated_table
    # strip trailing newlines and append two (row end + blank line)
    updated_table = updated_table.rstrip("\n") + "\n\n"

    updated_content = content[:table_start] + updated_table + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Tabella aggiornata con {update_count} sistemi!")

if __name__ == "__main__":
    update_about_table("about/index.md")