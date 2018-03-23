## Synopsis

The goal of this project is to provide insight into the current state of League of Legends champions and their effects on the likelihood of a match victory.

**Vision**

Allow a user to input a summoner's name (gamer tag) that's in an ongoing game and return the odds of each team winning the current match (and whether a team should surrender at 20 minutes).

**Mission**

Provide insight into the current state of League of Legends' champions and its effects on the likelihood of victory.

**Success Criteria**

A predicted win rate for a current match with an accuracy of above 50% (training on past, completed matches).

## Getting Started		

1. Clone surrender20 repository.

2. Create conda environment. 

    `conda create -n myenv python=3`
    
3. Activate environment.

    `source activate myenv`
	
   Windows Users:

    `activate myenv`

4. Install required packages. 

    `pip install -r requirements.txt`

5. Navigate to surrender20/development/src/models and run train_model.py script. This will process the external data and export to surrender20/development/models.

	`python train_model.py`

6. Navigate to surrender20/ and create a config.py file, writing the following line:
     
    `import os`
    
7. You are now ready to run the flask app.

	`python application.py`

## Using surrender20
For more information on how the functions used and how this application works, see the documentation in 

`development/docs/_build/html/index.html`.

## Running Unit Tests
Unit tests are located in  `development/function_tests.py`. To execute the tests, navigate to `development` in Terminal and run them with the following code:

`pytest function_tests.py`

## API Reference

Data is taken from one of two APIs:
Riot Games' League of Legends API, found here: https://developer.riotgames.com/.
Champion.gg's API, found here: http://api.champion.gg/.


## Contributors

Developer: Christa Spieth

Product Owner: Wenze Hu

Quality Assurance: Michael Gao

