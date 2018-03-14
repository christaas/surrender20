import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

# from clean_data import clean_data
# from get_info import get_info


def predict_response(user_input):
    """
    This function returns which team is predicted to win based on user's chosen match.
    Args:
        user_input (int): game id
    Returns:
        response_output: predicted winning team to be displayed on web app
    """
    # load pickle vectorizer & classifier
    classifier = joblib.load('./development/cl.pkl')
    # vectorize the input
    predictors_input = get_info([user_input])
    predictors_input = clean_data(predictors_input)
    predictors_input.toarray()
    # predict response
    response_output_raw = ''.join(classifier.predict(predictors_input))
    response_output = response_output_raw.capitalize().split('_')[0]
    return response_output
