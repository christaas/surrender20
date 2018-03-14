import keys
import requests
import json
import pandas as pd

API_KEY = keys.RIOT_KEY


# summonerName = 'Imaqtpie'
# summonerName = 'STUNNED'

def get_game(summonerName):
    '''Return a df with specified summoner information from ongoing game for model.'''
    # get summonerId
    summ_response = requests.get('https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/' + summonerName + '?api_key=' + API_KEY)
    try:
        summ_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # not a 200 status code
        print('sorry')
    # 200 status code
    summ_data = summ_response.json()
    summonerId = summ_data['id']

    # current match data
    match_response = requests.get('https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/' + str(summonerId) + '?api_key=' + API_KEY)
    try:
        match_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # not a 200 status code
        print('sorry')
    # 200 status code
    match_data = match_response.json()
    gameId = match_data['gameId']

    # get summoner names, champs
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

