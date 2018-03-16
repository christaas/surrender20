import os
import pandas as pd
import sklearn
import numpy
# uncomment lines below for sphinx
# import sys
# sys.path.append('src')
# from features.clean_training_data import clean_training_data
# from input.clean_input_data import clean_input_data
# from models.predict_response import predict_response
from development.src.features.clean_training_data import clean_training_data
from development.src.input.clean_input_data import clean_input_data
from development.src.models.predict_response import predict_response

games_path = os.path.dirname( __file__ ) + '/data/interim/game_info.csv'
champs_path = os.path.dirname( __file__ ) + '/data/interim/cgg.csv'

team1_champs = [4, 28, 27, 81, 43]
team2_champs = [134, 2, 29, 25, 50]
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
input_df = pd.DataFrame(columns=champ_names, data=[team1_champs + team2_champs])


def test_clean_training_data():
	df, scaler = clean_training_data(games_path, champs_path)
	assert type(df) is pd.core.frame.DataFrame
	assert type(scaler) is sklearn.preprocessing.data.StandardScaler
	assert len(df.columns) == 13


def test_clean_input_data():
	output_df = clean_input_data(input_df, champs_path)
	assert type(output_df) is pd.core.frame.DataFrame
	assert len(output_df) == 1
	assert len(output_df.columns) == 12


def test_predict_response():
	pred, prob = predict_response(input_df)
	assert type(pred) is int
	assert type(prob) is numpy.ndarray
	assert type(prob[0]) is numpy.ndarray
	assert (pred == 1 or pred == 2)
	assert len(prob[0]) == 2

