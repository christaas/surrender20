from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
#from flask_sqlalchemy import SQLAlchemy
from app import application
from development.src.models.predict_response import predict_response
from development.src.input.get_game import get_game


# home page
@application.route('/')
def index():

	return render_template("index.html")


# results page
@application.route('/results', methods=['GET', 'POST'])
def results():
	user_input = request.form['summName']
	df, team_1, team_2 = get_game(user_input)
	result, prob = predict_response(df)

	if result == 1:
		team_win = team_1
		team_lose = team_2
		prob_win = prob[0][0] * 100
		prob_lose = prob[0][1] * 100

	else:
		team_win = team_2
		team_lose = team_1
		prob_win = prob[0][1] * 100
		prob_lose = prob[0][0] * 100

	return render_template("results.html", team_win =team_win, team_lose=team_lose, prob_win=prob_win, prob_lose=prob_lose)


if __name__ == "__main__":
	application.run(host='0.0.0.0', debug=True)
