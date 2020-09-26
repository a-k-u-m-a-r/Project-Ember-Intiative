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

app_key = {
    "type" : "service_account",
    "project_id" : os.environ.get("PROJECT_ID"),
    "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
    "private_key": os.environ.get("PRIVATE_KEY").replace("\\n", "\n"),
    "client_email" : os.environ.get("CLIENT_EMAIL"),
    "client_id" : os.environ.get("CLIENT_ID"),
    "auth_uri" : os.environ.get("AUTH_URI"),
    "token_uri" : os.environ.get("TOKEN_URI"),
    "auth_provider_x509_cert_url": os.environ.get("AUTH_PROVIDER"),
    "client_x509_cert_url": os.environ.get("CLIENT_URL")
}

#app_key = "C:\\Users\\emu4y\\Documents\\GitHub\\Project-BC\\key.json"

app.config.from_object('app.configuration.Config')
cred = credentials.Certificate(app_key) #Switch when Deploying "/Users/akshaykumar/Documents/Projects/FlaskLearning/db_example/key.json"
firebase_admin.initialize_app(cred)

# Import routing, models and Start the App
from app import views, models
