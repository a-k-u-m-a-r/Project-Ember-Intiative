# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
# FIND A WAY TO REPLACE THIS FILE
import os
import firebase_admin

from flask            import Flask
from firebase_admin   import credentials, firestore

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.from_object('app.configuration.Config')
cred = credentials.Certificate("/Users/akshaykumar/Documents/Projects/FlaskLearning/db_example/key.json") #make path an ENVIRON VAR
firebase_admin.initialize_app(cred)

# Import routing, models and Start the App
from app import views, models
