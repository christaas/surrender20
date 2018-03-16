from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib


def train_model(training_df, scaler):
    """
    This function fits a logistic regression model on the training data to classify either a win or loss.
    It creates a pickle file for the model so that it can be used for prediction.

    Arg:
      training_df (DataFrame): data to be used for fitting the model

    Returns:
      cl.pkl: classifier stored as pickle file to be used for prediction
    """

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
    joblib.dump(classifier, 'cl.pkl')
    joblib.dump(scaler, 'scaler.pkl')



