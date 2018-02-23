import requests
import json
import csv
import config

API_KEY = config.API_KEY

## get list of challenger player summonerIds
challenger_response = requests.get('https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=' + API_KEY)
challenger_data = challenger_response.json()['entries']
challenger_players = []
for num in list(range(0,50)):
	summonerId = challenger_data[num]['playerOrTeamId']
	challenger_players.append(summonerId)
print(challenger_players)

with open('challenger.csv', 'w') as f:
    c = csv.writer(f)

    for player in challenger_players:
    	c.writerow([player])