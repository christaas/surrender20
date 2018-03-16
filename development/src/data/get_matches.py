import csv
import time

import pandas as pd
import requests

import config

API_KEY = config.RIOT_KEY

accountIds = pd.read_csv('challenger_aid.csv', header=None)[0].tolist()
matchIds = set()

for accountId in accountIds:
	try:
		match_response = requests.get('https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/' + str(accountId) + '?beginTime=1519300800000&api_key=' + API_KEY)
		match_data = match_response.json()['matches']
		for match in match_data:
			matchIds.add(match['gameId'])
	except KeyError as e:
		continue
	finally:
		time.sleep(1.3)

with open('matches.csv', 'w') as f:
    c = csv.writer(f)

    for matchId in matchIds:
    	c.writerow([matchId])

# pprint(matchIds)

