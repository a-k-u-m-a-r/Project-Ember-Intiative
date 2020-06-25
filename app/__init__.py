# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
import firebase_admin

from flask            import Flask
from firebase_admin   import credentials
from firebase_admin   import firestore

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.configuration.Config')
cred = credentials.Certificate("/Users/akshaykumar/Documents/Projects/FlaskLearning/db_example/key.json") #make path an ENVIRON VAR
firebase_admin.initialize_app(cred)


# db = SQLAlchemy  (app) # flask-sqlalchemy
# bc = Bcrypt      (app) # flask-bcrypt

# lm = LoginManager(   ) # flask-loginmanager
# lm.init_app(app) # init the login manager

# Setup database
# @app.before_first_request
# def initialize_database():
#     db.create_all()

# Import routing, models and Start the App
from app import views, models
