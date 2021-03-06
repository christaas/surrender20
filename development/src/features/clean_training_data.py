import pandas as pd
from sklearn import preprocessing as prep
import logging

logging.basicConfig(level=logging.INFO)


def clean_training_data(games_path, champs_path):
	"""Return a cleaned DataFrame for model training.

	:param games_path: path to Riot Games game training data file
	:param champs_path: path to Champion.gg champion training data file
	:return: formatted training DataFrame
	"""
	logger = logging.getLogger(__name__)

	# import data
	logging.debug('Loading data from %s and %s.', games_path, champs_path)
	games = pd.read_csv(games_path)
	champs = pd.read_csv(champs_path)

	def drop_y(dataframe):
		# list comprehension of the columns that end with '_drop'
		to_drop = [x for x in dataframe if x.endswith('_drop')]
		dataframe.drop(to_drop, axis=1, inplace=True)

	# get needed references for stats collection
	logging.info('Defining predictor and response columns.')
	champ_names = list(games)[2:12]
	var_name = champs.columns[1:13]
	var_num = range(1, 13)
	df = games

	# cumulative stats for each team
	logging.info('Getting cumulative stats for each team.')
	for j in range(0, len(var_name)):
		logging.debug('Aggregating stats for %s.', var_name[j])

		# merge games df with champion df for each stat
		for i in range(0, 10):
			df = pd.merge(df, champs.iloc[:, [0, var_num[j]]], left_on=champ_names[i], right_on='championId',
						  suffixes=['_drop', '_drop'])
			df.rename(columns={var_name[j]: var_name[j] + str(i + 1)}, inplace=True)

		# drop duplicate columns created from merge
		drop_y(df)

		# aggregate stats for team 1
		df['t1'] = df.iloc[:, -10:-5].sum(axis=1)
		df = df.drop(df.iloc[:, -11:-6], axis=1)

		# aggregate stats for team 2
		df['t2'] = df.iloc[:, -6:-1].sum(axis=1)
		df = df.drop(df.iloc[:, -7:-2], axis=1)

		# take the stats difference between teams in reference to team 1
		df['diff'] = df['t1'] - df['t2']
		df.rename(columns={'diff': var_name[j]}, inplace=True)

		# drop now unneeded 't1' and 't1' columns
		df = df.drop(['t1', 't2'], axis=1)

	# drop gameId and champion id columns
	df = df.drop(['gameId'], axis=1)
	df = df.drop(df.iloc[:, 1:11], axis=1)

	# standardize predictors
	logging.info('Standardizing predictors.')
	scaler = prep.StandardScaler().fit(df.iloc[:, 1:])
	df.iloc[:, 1:] = pd.DataFrame(prep.scale(df.iloc[:, 1:]), columns=df.iloc[:, 1:].columns,
								  index=df.iloc[:, 1:].index)

	return df, scaler
