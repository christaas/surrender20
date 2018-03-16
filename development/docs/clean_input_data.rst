Clean Input Data
=======================

After getting a DataFrame of each team's champions using :meth:`get_game()`, this function gathers the statistics relative to team 1 for both teams. For example, :meth:`clean_input_data` will add up the champion win rates for each team, take the difference team win rates relative to team 1, and then standardize the predictors using the scaler.pkl created by :meth:`train_model()`.

.. automodule:: clean_input_data
	:members: