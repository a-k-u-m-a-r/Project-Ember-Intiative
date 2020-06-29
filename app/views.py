# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort, BadRequestKeyError

# App modules
from app        import app
from app.models import User
from app.forms  import LoginForm, RegisterForm

# Firestore
from firebase_admin import firestore

user = User()
db = firestore.client()
#Index Route
@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/profile')
def profile():
    return render_template('pages/profile.html')

@app.route('/courses')
def courses():
    return render_template('pages/courses.html')

@app.route('/components')
def components():
    return render_template('pages/components.html')

@app.route('/machine-learning', methods=['GET', 'POST'])
def ml():
    #Make this stuff into a function
    hidden_vals = ['numcorrect', 'numcorrect2']
    if request.method == 'POST':  #this block is only entered when the form is submitted
        for hidden_val in hidden_vals:
            try:
                db.collection(u'users').document(session['uname']).collection(u'courses').document(u'machine-learning').update({hidden_val: int(request.form[hidden_val])})
                print("WE did it obiz")
            except BadRequestKeyError:
                pass
    return render_template('pages/machinel.html')

@app.route('/swift', methods=['GET', 'POST'])
def swift():
    hidden_vals = ['numcorrect', 'numcorrect2']
    if request.method == 'POST':  #this block is only entered when the form is submitted
        for hidden_val in hidden_vals:
            try:
                db.collection(u'users').document(session['uname']).collection(u'courses').document(u'swift').update({hidden_val: int(request.form[hidden_val])})
                print("WE did it obiz")
            except BadRequestKeyError:
                pass
    return render_template('pages/swift.html')

@app.route('/electrical-engineering', methods=['GET', 'POST'])
def ee():
    hidden_vals = ['numcorrect', 'numcorrect2']
    if request.method == 'POST':  #this block is only entered when the form is submitted
        for hidden_val in hidden_vals:
            try:
                db.collection(u'users').document(session['uname']).collection(u'courses').document(u'electrical-engineering').update({hidden_val: int(request.form[hidden_val])})
                print("WE did it obiz")
            except BadRequestKeyError:
                pass
    return render_template('pages/electroeg.html')

@app.route('/article', methods=['GET', 'POST'])
def article():
    hidden_vals = ['numcorrect', 'numcorrect2']
    if request.method == 'POST':  #this block is only entered when the form is submitted
        for hidden_val in hidden_vals:
            try:
                db.collection(session['uname']).document(u'python').update({hidden_val: request.form[hidden_val]})
                print("WE did it obiz")
            except BadRequestKeyError:
                pass
                
    return render_template('pages/article-template.html')


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
        
        doc_ref = db.collection(u'users').document(username)
        doc_ref.set({
            u'uname': username,
        })

        # Make this into function
        ml_ref = db.collection(u'users').document(username).collection(u'courses').document(u'machine-learning')
        ml_ref.set({
            u'numcorrect': 0.0,
            u'numcorrect2': 0.0,
            u'progress': 0.0,
            u'totalpoints': 6.0
        })

        swift_ref = db.collection(u'users').document(username).collection(u'courses').document(u'swift')
        swift_ref.set({
            u'numcorrect': 0.0,
            u'numcorrect2': 0.0,
            u'progress': 0.0,
            u'totalpoints': 6.0
        })

        ee_ref = db.collection(u'users').document(username).collection(u'courses').document(u'electrical-engineering')
        ee_ref.set({
            u'numcorrect': 0.0,
            u'numcorrect2': 0.0,
            u'progress': 0.0,
            u'totalpoints': 6.0
        })
    

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





