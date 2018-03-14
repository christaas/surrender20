import pandas as pd
from sklearn import preprocessing as prep
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib


def clean_input_data(input_df, champs_path):
    """
    This function creates a cleaned DataFrame from json file training data

    Args:
        input_df (df): user input df that needs to be cleaned for the model
        champs_path (str): path to Champion.gg champion training data file
    Returns:
        df: cleaned user input
    """

    def drop_y(dataframe):
        # list comprehension of the columns that end with '_drop'
        to_drop = [x for x in dataframe if x.endswith('_drop')]
        dataframe.drop(to_drop, axis=1, inplace=True)

    # import data
    scaler = joblib.load('scaler.pkl')
    champs = pd.read_csv(champs_path)

    # get needed references for stats collection
    champ_names = list(input_df)
    var_name = champs.columns[1:13]
    var_num = range(1, 13)

    # cumulative stats for each team
    for j in range(0, len(var_name)):

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
    df = df.drop(df.iloc[:, 0:10], axis=1)

    # standardize predictors
    df = pd.DataFrame(scaler.transform(df), columns=df.columns,
                      index=df.index)

    return df
