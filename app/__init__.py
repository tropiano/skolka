# all the imports
from flask import Flask, g, render_template, send_file, jsonify, session, abort, request, flash, redirect, url_for
import requests as r
import os
# from wtforms import Form, BooleanField, StringField, FloatField, DateField, IntegerField, validators


app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)
# uncomment to test locally
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/fpl'
# db.Model.metadata.reflect(db.engine)
app.secret_key = 'T5%&/yHDfSTs'

# views


@app.route('/', methods=['GET'])
def home_page():

    # 9000 eur to rub
    q_9eur = r.get(
        "https://api.sandbox.transferwise.tech/v1/quotes?source=EUR&target=RUB&sourceAmount=9000&rateType=FIXED")
    # 10000 eur to rub
    q_10eur = r.get(
        "https://api.sandbox.transferwise.tech/v1/quotes?source=EUR&target=RUB&sourceAmount=10000&rateType=FIXED")
    # 3000 eur to rub
    q_3eur = r.get(
        "https://api.sandbox.transferwise.tech/v1/quotes?source=EUR&target=RUB&sourceAmount=3000&rateType=FIXED")
    # 9000 gbp to rub
    q_9gbp = r.get(
        "https://api.sandbox.transferwise.tech/v1/quotes?source=GBP&target=RUB&sourceAmount=9000&rateType=FIXED")

    total_rub = 2*q_9eur.json()["targetAmount"] + q_10eur.json()["targetAmount"] + \
        2*q_3eur.json()["targetAmount"] + q_9gbp.json()["targetAmount"]

    return render_template('index.html', entries=total_rub)
