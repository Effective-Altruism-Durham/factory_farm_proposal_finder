import os
import requests
import csv

def filter1_permits():
    try:
        print('nothing unhinged is happening')
        # UPDATE THE URL
        url = "https://environment.data.gov.uk/public-register/industrial-installations/registration.json?_limit=1000"
        response = requests.get(url)
        if (response.status_code == 200):
            people_who_can_farm = []
            print('good response')
            permitHolders = response.json()
            for permitHolder in permitHolders["items"]:
                try:
                    single_farmer = {"activity": permitHolder["activity"][0]["comment"],
                                     "name": permitHolder["holder"]["name"],
                                     "postcode": permitHolder["site"]["siteAddress"]["postcode"],
                                     "organization": permitHolder["site"]["siteAddress"]["organization_name"]}
                except:
                    single_farmer = {"activity": permitHolder["activity"]["comment"],
                                     "name": permitHolder["holder"]["name"],
                                     "postcode": permitHolder["site"]["siteAddress"]["postcode"],
                                     "organization": permitHolder["site"]["siteAddress"]["organization_name"]}
                if 'Intensive' in (single_farmer['activity']):
                    people_who_can_farm.append(single_farmer)
        else:
            print("Error: File does not exist")
        return(people_who_can_farm)
    except requests.exceptions.RequestException:
        print("Error: Could not connect to server") 
        return(None)

print(filter1_permits())

'''
        for row in reader:
            if row[5] == match_string:
                activity = row[2] 
            if (activity == 'Intensive Farming; > 40,000 Poultry -  6.9 A(1) a) (i)') or (activity == 'Directly Associated Activity (Included)|Intensive Farming; > 2,000 Pigs (Production Pigs) -  6.9 A(1) a) (ii)') or (activity == 'Intensive Farming; > 2,000 Pigs (Production Pigs) -  6.9 A(1) a) (ii)'):
                return True
        return None  # Return None if no match is found

url = "https://www.planit.org.uk/api/applics/json?app_state=Undecided&app_state=Other&app_type=Outline&app_type=Amendment&app_type=Other&recent=80&search=livestock%20OR%20dairy%20OR%20egg%20OR%20milk%20OR%20meat%20OR%20poultry%20OR%20pig%20OR%20cattle%20OR%20husbandry%20OR%20cattle%20OR%20swine%20OR%20goats%20OR%20sheep%20OR%20farm%20OR%20free-range%20OR%20barn%20OR%20cull%20OR%20dairy%20OR%20milk%20OR%20beef%20OR%20pork%20OR%20lamb%20OR%20antibiotic%20OR%20slaughterhouse%20OR%20broiler%20OR%20cage%20OR%20cow%20OR%20pork%20OR%20lamb%20OR%20turkey%20OR%20duck%20OR%20goat%20OR%20aquaculture%20OR%20hatchery%20OR%20intensive%20OR%20salmon%20OR%20tilapia%20OR%20trout%20OR%20catfish%20OR%20cod%20OR%20carp%20OR%20barramundi%20OR%20bass%20OR%20shrimp%20OR%20mollusk%20OR%20oyster%20OR%20baitfish%20OR%20aquafeed%20OR%20incubation%20OR%20fingerlings%20OR%20spawning%20OR%20slaughter%20OR%20fillet"
try:
    response = requests.get(url)
    if (response.status_code == 200):
        proposals = response.json()
        for i in proposals["records"]:
            print(i["description"])
            print(i["url"])
            match_string = i["postcode"]
            if filter1_permits(match_string) == True:
                print(match_string)
    else:
        print("Error: File does not exist")
except requests.exceptions.RequestException:
    print("Error: Could not connect to server")

'''