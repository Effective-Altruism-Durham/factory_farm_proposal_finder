import os
import requests
url = "https://www.planit.org.uk/api/applics/json?app_state=Undecided&app_state=Other&app_type=Outline&app_type=Amendment&app_type=Other&recent=80&search=livestock%20OR%20dairy%20OR%20egg%20OR%20milk%20OR%20meat%20OR%20poultry%20OR%20pig%20OR%20cattleOR%20husbandryOR%20cattleOR%20poultryOR%20swineOR%20goatsOR%20sheepOR%20farmOR%20free-rangeOR%20barnOR%20cullOR%20dairyOR%20milkOR%20beefOR%20porkOR%20lambOR%20antibioticOR%20slaughterhouse"

try:
    response = requests.get(url)
    if (response.status_code == 200):
        proposals = response.json()
        for i in proposals["records"]:
            print(i["description"])
            print(i["url"])
            print(i["uid"])
            print('')
    else:
        print("Error: File does not exist")
except requests.exceptions.RequestException:
    print("Error: Could not connect to server")