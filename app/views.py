# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort

# App modules
from app        import app
from app.models import User
from app.forms  import LoginForm, RegisterForm


user = User()

#Index Route
@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/profile')
def profile():
    return render_template('pages/profile.html')

@app.route('/components')
def components():
    return render_template('pages/components.html')

@app.route('/article')
def article():
    return render_template('pages/article.html')

# Register a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    
    # declare the Registration Form
    form = RegisterForm(request.form)

    msg = None

    if request.method == 'GET': 

        return render_template( 'accounts/register.html', form=form, msg=msg )

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str) 
        email = request.form.get('email', '', type=str) 
        

        user.create_user(email, password, username)
        
        print(f"The username is: {username} and the password is: {password}. The email is {email}")
        return redirect(url_for('index'))

        #Error Processing: !     
 
    return render_template( 'accounts/register.html', form=form, msg=msg )

# Authenticate user
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # Declare the login form
    form = LoginForm(request.form)

    # Flask message injected into the page, in case of any errors
    msg = None

    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():

        # assign form data to variables
        email = request.form.get('username', '', type=str) #Change this from username to email
        password = request.form.get('password', '', type=str) 

        #Make it so that it raises errors <- any error messages are returned to msg
        msg = user.login_user(email, password)

        if msg != None:
             return render_template( 'accounts/login.html', form=form, msg=msg )
        return redirect(url_for('index'))


    return render_template( 'accounts/login.html', form=form, msg=msg )

# Logout user
@app.route('/logout')
def logout():
    user.logout_user()
    return redirect(url_for('index'))





