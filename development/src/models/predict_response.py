import os
from sklearn.externals import joblib
from development.src.input.clean_input_data import clean_input_data


def predict_response(user_input):
	"""
	This function returns which team is predicted to win based on user's chosen match.
	Args:
		user_input (int): game id
	Returns:
		response_output: predicted winning team to be displayed on web app
	"""
	# load pickle classifier
	classifier = joblib.load(os.path.dirname(os.path.dirname(os.path.dirname( __file__ ))) + '/models/cl.pkl')
	# get predictors
	predictors_input = user_input
	predictors_input = clean_input_data(predictors_input, os.path.dirname(os.path.dirname(os.path.dirname( __file__ ))) + '/data/interim/cgg.csv')
	# predict response
	response_output = int(classifier.predict(predictors_input))
	response_prob = classifier.predict_proba(predictors_input)

	return response_output, response_prob

