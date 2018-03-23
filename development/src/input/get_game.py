import pandas as pd
import requests
# for sphinx, uncomment lines below
# import sys
# sys.path.append('../')
# from src import keys
from development.src import keys
import logging

logging.basicConfig(level=logging.INFO)
API_KEY = keys.RIOT_KEY


def get_game(summonerName):
	"""Return a DataFrame with specified summoner's game information from ongoing game for model.

	:param summonerName: name of player in ongoing game
	:return: DataFrame of champions on each team, list of team 1's players, list of team 2's players
	"""
	logger = logging.getLogger(__name__)

	# get summonerId
	logging.info('Attempting to find summonerId for %s.', summonerName)
	summ_response = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summonerName + '?api_key=' + API_KEY)
	try:
		summ_response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		# not a 200 status code
		logging.info('Summoner %s not found.', summonerName)
	# 200 status code
	summ_data = summ_response.json()
	summonerId = summ_data['id']

	# current match data
	logging.info('Attempting to find current game for %s.', summonerName)
	match_response = requests.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + str(summonerId) + '?api_key=' + API_KEY)
	try:
		match_response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		# not a 200 status code
		logging.info('Game not found.')
	# 200 status code
	match_data = match_response.json()

	# get summoner names, champs
	logging.debug('Formatting game information.')
	team1_champs = []
	team1_players = []
	team2_champs = []
	team2_players = []
	for num in list(range(0, 10)): # number of players
		if match_data['participants'][num]['teamId'] == 100:
			team1_champs.append(match_data['participants'][num]['championId'])
			team1_players.append(match_data['participants'][num]['summonerName'])
		else:
			team2_champs.append(match_data['participants'][num]['championId'])
			team2_players.append(match_data['participants'][num]['summonerName'])
	champ_names = ['team1_champ1',
					'team1_champ2',
					'team1_champ3',
					'team1_champ4',
					'team1_champ5',
					'team2_champ1',
					'team2_champ2',
					'team2_champ3',
					'team2_champ4',
					'team2_champ5']
	df = pd.DataFrame(columns=champ_names, data=[team1_champs+team2_champs])

	return df, team1_players, team2_players

