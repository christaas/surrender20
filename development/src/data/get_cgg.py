import requests
import json
import csv
import config
import pandas as pd
from pprint import pprint

API_KEY = config.CGG_KEY

df = {}

stats_response = requests.get('http://api.champion.gg/v2/champions?champData=matchups,goldEarned,damage,overallPerformanceScore,kda,winRate&limit=500&api_key=' + API_KEY)
stats_data = stats_response.json()

for champion in stats_data:
	championId = champion['championId']
	winRate = champion['winRate']
	banRate = champion['banRate']
	gamesPlayed = champion['gamesPlayed']
	playRate = champion['playRate']
	kills = champion['kills']
	deaths = champion['deaths']
	assists = champion['assists']
	score = champion['overallPerformanceScore']
	gold = champion['goldEarned']
	damageTaken = champion['totalDamageTaken']
	totalHeal = champion['totalHeal']
	totalDamage = champion['damageComposition']['total']

	
	for role in champion['matchups']:
		
		for matchup in champion['matchups'][role]:
			rivals = set()

			if matchup['champ1_id'] == championId:
				winrate = matchup['champ1']['winrate']
				rival = matchup['champ2_id']
			else:
				winrate = matchup['champ2']['winrate']
				rival = matchup['champ1_id']

			if winrate <= .45:
				rivals.add(rival)

			if championId in df:
				average = df[championId][2] + gamesPlayed

				df[championId][0] = (winRate*gamesPlayed + df[championId][0]*df[championId][2]) / average
				df[championId][4] = (kills*gamesPlayed + df[championId][4]*df[championId][2]) / average
				df[championId][5] = (deaths*gamesPlayed + df[championId][5]*df[championId][2]) / average
				df[championId][6] = (assists*gamesPlayed + df[championId][6]*df[championId][2]) / average
				df[championId][7] = (score*gamesPlayed + df[championId][7]*df[championId][2]) / average
				df[championId][8] = (gold*gamesPlayed + df[championId][8]*df[championId][2]) / average
				df[championId][9] = (damageTaken*gamesPlayed + df[championId][9]*df[championId][2]) / average
				df[championId][10] = (totalHeal*gamesPlayed + df[championId][10]*df[championId][2]) / average
				df[championId][11] = (totalDamage*gamesPlayed + df[championId][11]*df[championId][2]) / average

				df[championId][2] += gamesPlayed
				df[championId][3] += playRate

				df[championId][12].update(rivals)
			else:
				df[championId] = [winRate, banRate, gamesPlayed, playRate, kills, deaths, assists, 
					score, gold, damageTaken, totalHeal, totalDamage, rivals]

headers = ['championId', 'winRate', 'banRate', 'gamesPlayed', 'playRate', 'kills', 
	'deaths', 'assists', 'score', 'gold', 'damageTaken', 'totalHeal', 'totalDamage', 'rivals']

with open('cgg.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key, value in df.items():
            writer.writerow({'championId': key, 
            	'winRate': value[0], 
            	'banRate': value[1], 
            	'gamesPlayed': value[2], 
            	'playRate': value[3], 
            	'kills': value[4], 
				'deaths': value[5], 
				'assists': value[6], 
				'score': value[7], 
				'gold': value[8], 
				'damageTaken': value[9], 
				'totalHeal': value[10], 
				'totalDamage': value[11], 
				'rivals': value[12]})

# pprint(df.keys())