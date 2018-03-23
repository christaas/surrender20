import os
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
# uncomment the lines below for sphinx
# import sys
# sys.path.append('../features')
# from clean_training_data import clean_training_data
from development.src.features.clean_training_data import clean_training_data
import logging

logging.basicConfig(level=logging.INFO)


def train_model():
	"""Fit a logistic regression model on the training data to classify either a win or loss.

	:return: two pickle files for the prediction model, :file:`cl.pkl` and :file:`scaler.pkl`
	"""
	logger = logging.getLogger(__name__)

	# data paths
	games_path = '/data/interim/game_info.csv'
	champs_path = '/data/interim/cgg.csv'
	# clean data
	logger.info('Cleaning training data located at %s and %s.', games_path, champs_path)
	training_df, scaler = clean_training_data(games_path, champs_path)
	# define predictors
	logger.debug('Defining predictors.')
	predictors = training_df.loc[:, training_df.columns != 'team_win']
	# define response
	logger.debug('Defining response.')
	response = training_df['team_win']
	# instantiate model
	clf = LogisticRegression()
	# train the model
	logger.debug('Training model.')
	parameters = {'C': [1, 10]}
	classifier = GridSearchCV(clf, parameters)
	classifier = classifier.fit(predictors, response)
	# create pickle files
	logger.info('Saving model and scaler at /models/cl.pkl and /models/scaler.pkl.')
	joblib.dump(classifier, '/models/cl.pkl')
	joblib.dump(scaler, os.path.dirname(os.path.dirname(__file__)) + '/models/scaler.pkl')
