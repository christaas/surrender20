import csv
import time

import pandas as pd
import requests

from development.src import keys

API_KEY = keys.RIOT_KEY

df = {}
teamIds = ['100', '200']

gameIds = pd.read_csv('~/Desktop/s20/matches.csv', header=None, names=['gameId'])

for gameId in gameIds['gameId']:
    print(gameId)

    try:
        match_response = requests.get('https://na1.api.riotgames.com/lol/match/v3/matches/' + str(gameId) + '?api_key=' + API_KEY)
        match_data = match_response.json()

        teamChampions = {key: [] for key in teamIds}

        if match_data['mapId'] == 11:
            for team in match_data['teams']:
                if team['win'] == 'Win':
                    win = team['teamId']

            for player in match_data['participants']:
                team = str(player['teamId'])
                champion = player['championId']
                teamChampions[team].append(champion)

            df[gameId] = [int(win/100), teamChampions['100'][0], teamChampions['100'][1], teamChampions['100'][2], 
                teamChampions['100'][3], teamChampions['100'][4], teamChampions['200'][0], teamChampions['200'][1], 
                teamChampions['200'][2], teamChampions['200'][3], teamChampions['200'][4]]
    except:
        continue
    finally:
        time.sleep(1.3)

# write to csv
headers = ['gameId', 'team_win', 'team1_champ1', 'team1_champ2', 'team1_champ3', 'team1_champ4', 
    'team1_champ5', 'team2_champ1', 'team2_champ2', 'team2_champ3', 'team2_champ4', 'team2_champ5']


with open('game_info.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key, value in df.items():
            writer.writerow({'gameId': key, 
                'team_win': value[0], 
                'team1_champ1': value[1], 
                'team1_champ2': value[2], 
                'team1_champ3': value[3], 
                'team1_champ4': value[4], 
                'team1_champ5': value[5], 
                'team2_champ1': value[6], 
                'team2_champ2': value[7], 
                'team2_champ3': value[8], 
                'team2_champ4': value[9], 
                'team2_champ5': value[10]})
