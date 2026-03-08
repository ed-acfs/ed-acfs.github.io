import requests
from urllib.parse import quote

system_name = "Sol"
encoded_name = quote(system_name)
url = f"https://www.edsm.net/api-v1/systems?systemName={encoded_name}&showInformation=1"
print(f"URL: {url}")
response = requests.get(url)
print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    if data and isinstance(data, list) and len(data) > 0:
        system_data = data[0]
        info = system_data.get('information', {})
        population = info.get('population', 0)
        print(f"Data: {system_data}")
        print(f"Popolazione: {population}")
    else:
        print("Nessun dato trovato")
else:
    print(f"Errore: {response.text[:500]}")