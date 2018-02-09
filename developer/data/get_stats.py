import config
import requests
import json
import csv
import pandas as pd

API_KEY = config.API_KEY

## database of champion names and keys (for display)
champs = pd.read_csv('~/Desktop/s20/champions.csv', header=None, names=['key', 'name'], index_col = 0)

## database of challenger player summonerIds
challenger_players = pd.read_csv('~/Desktop/s20/challenger.csv', header=None, names=['summonerId'])

## find first player that has an ongoing game
for index, player in challenger_players.iterrows():
    match_response = requests.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + str(player['summonerId']) + '?api_key=' + API_KEY)
    try:
        match_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # not a 200 status code
        continue
    # 200 status code
    match_data = match_response.json()
    break
# print(match_data)

## get summoner names, champs 
names = {} # summonerId : summonerName, championId, championName
for num in list(range(0,9)): # number of players
  names[str(match_data['participants'][num]['summonerId'])] \
  = [str(match_data['participants'][num]['summonerName']), \
    str(match_data['participants'][num]['championId']), \
    champs.loc[match_data['participants'][num]['championId']]['name']]
# print(names)

## find champion masteries for each player
mastery_db = {}
for player in names.keys():
    # print(names[player][1])
    mastery_response = requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v3/champion-masteries/by-summoner/' + player + '/by-champion/' + names[player][1] + '?api_key=' + API_KEY)
    mastery_data = mastery_response.json()
    # print(mastery_data)
    champion_pts = mastery_data['championPoints']
    last_played = mastery_data['lastPlayTime']
    mastery_db[player] = [champion_pts, last_played]
print(mastery_db)