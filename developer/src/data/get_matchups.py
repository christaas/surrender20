import requests
import json
import csv
import config
from pprint import pprint

API_KEY = config.CGG_KEY

## get list of challenger player summonerIds
matchup_response = requests.get('http://api.champion.gg/v2/champions/1?limit=5&api_key=' + API_KEY)
matchup_data = matchup_response.json()
matchups = {}
for role in matchup_data:


	# matchups[1] = [str(match_data['participants'][num]['summonerName']), \
	# str(match_data['participants'][num]['championId']), \
	# champs.loc[match_data['participants'][num]['championId']]['name'], \
	# str(match_data['participants'][num]['teamId'])]



# 	matchups.append(champion_matchup)


	pprint(role['role'] + ' ' + str(role['winRate']) + ' ' + str(role['gamesPlayed']))

# pprint(matchups)