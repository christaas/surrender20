import requests
import json
import csv
import config

## update key as needed
API_KEY = config.API_KEY

## database of champion names and keys (for display)
champions_static = requests.get('http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json')
champions_db = champions_static.json()['data']
champs = {}  # championID : champion name 
for champion in champions_db:
	champs[int(champions_db[champion]['key'])] = champions_db[champion]['name']
# print(champs)

with open('champions.csv', 'w') as f:
    c = csv.writer(f)

    for key, value in champs.items():
        c.writerow([key, value])