Getting Started
===============

You will need to get API keys for both Riot Games' API and Champion.gg's API and store them in a file called :file:`keys.py`. After obtaining the API keys, the scripts in :file:`surrender20/development/src/data` should be run in the following order:

#. :file:`surrender20/development/src/data/get_matches.py`

#. :file:`surrender20/development/src/data/get_past_riot.py`

#. :file:`surrender20/development/src/data/get_cgg.py`

These scripts will produce the training data needed to use the rest of the :program:`surrender20` package and store the data in :file:`surrender20/development/data` directory.

**Note:** The champion statistics from Champion.gg will update every patch, so the timestamp in :file:`get_matches.py` must also be updated with the time of the newest patch release.

**Note:** The Riot Games' API key expires 24 hours after activation. Make sure to update daily!
