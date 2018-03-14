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
# @application.route('/results')
@application.route('/results', methods=['GET','POST'])
def results():
    # user_input = request.form['summonerName']
    # teams = get_game(user_input)
    # result = predict_response(teams)

    return render_template("results.html")
    # return render_template("results.html", result=result, teams=teams)


if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)