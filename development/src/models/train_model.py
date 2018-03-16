import os
import sys
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
sys.path.append('../features')
from clean_training_data import clean_training_data


def train_model():
	"""Fit a logistic regression model on the training data to classify either a win or loss.

	:return: two pickle files for the prediction model, :file:`cl.pkl` and :file:`scaler.pkl`
	"""

	# data paths
	# games_path = os.path.dirname(__file__) + '/data/interim/game_info.csv'
	games_path = '/data/interim/game_info.csv'
	champs_path = '/data/interim/cgg.csv'
	# clean data
	training_df, scaler = clean_training_data(games_path, champs_path)
	# define predictors
	predictors = training_df.loc[:, training_df.columns != 'team_win']
	# define response
	response = training_df['team_win']
	# instantiate model
	clf = LogisticRegression()
	# train the model
	parameters = {'C': [1, 10]}
	classifier = GridSearchCV(clf, parameters)
	classifier = classifier.fit(predictors, response)
	# create pickle files
	joblib.dump(classifier, '/models/cl.pkl')
	joblib.dump(scaler, os.path.dirname(os.path.dirname(__file__)) + '/models/scaler.pkl')
