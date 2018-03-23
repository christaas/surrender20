import os
from sklearn.externals import joblib
# uncomment the lines below for sphinx
# import sys
# sys.path.append('../input')
# from clean_input_data import clean_input_data
from development.src.input.clean_input_data import clean_input_data
import logging

logging.basicConfig(level=logging.INFO)


def predict_response(user_input):
	"""Return which team is predicted to win based on user's chosen match.

	:param user_input: game id
	:return: identifier of team (team 1 or team 2) predicted to win, probability of win for each team
	"""
	logger = logging.getLogger(__name__)

	# load pickle classifier
	model_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/models/cl.pkl'
	logging.info('Loading model pickle file from %s.', model_path)
	classifier = joblib.load(model_path)
	# get predictors
	champ_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/data/interim/cgg.csv'
	logging.info('Cleaning input data with champion data at %s.', model_path)
	predictors_input = user_input
	predictors_input = clean_input_data(predictors_input, champ_path)
	# predict response
	logging.debug('Predicting outcome.')
	response_output = int(classifier.predict(predictors_input))
	response_prob = classifier.predict_proba(predictors_input)

	return response_output, response_prob
