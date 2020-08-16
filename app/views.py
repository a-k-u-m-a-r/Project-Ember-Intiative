# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

# Python modules
import os, logging 

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory, session, make_response
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort, BadRequestKeyError

# App modules
from app        import app
from app.models import User
from app.constants import *
from app.forms  import LoginForm, RegisterForm
import os
# Firestore
from firebase_admin import firestore

user = User()
db = firestore.client()
#Index Route
@app.route('/')
def index():
    return render_template('pages/index.html')

@app.route('/about')
def about():
    return render_template('pages/aboutus.html')

@app.route('/contact-us')
def contactus():
    return render_template('pages/contactus.html')


@app.route('/coursehub')
def courses():
    if 'uname' not in session:
        return redirect(url_for('login'))
    return render_template('courses/courses.html')

@app.route('/components')
def components():
    return render_template('pages/components.html')

@app.route('/courses/python', methods=['GET', 'POST'])
def py():
    if 'uname' not in session:
        return redirect(url_for('index'))
    hidden_vals = py_course['courses']
    doc = user.getCourseDoc(session['uname'], u'python', db)

    if request.method == 'POST':
        user.assignmentCompleted(hidden_vals, session['uname'], u'python', db)
        return redirect(url_for('py'))

    session['py'] = user.getProgress(doc, py_course['courses'])
    return render_template('courses/python.html', doc=doc, py_course=py_course['courses'])

@app.route('/courses/swift', methods=['GET', 'POST'])
def swift():
    if 'uname' not in session:
        return redirect(url_for('index'))
    hidden_vals = sw_course['courses']
    doc = user.getCourseDoc(session['uname'], u'swift', db)

    if request.method == 'POST':
        user.assignmentCompleted(hidden_vals, session['uname'], u'swift', db)
        return redirect(url_for('swift'))

    session['sw'] = user.getProgress(doc, sw_course['courses'])
    return render_template('courses/swift.html', doc=doc, sw_course=sw_course['courses'])

@app.route('/courses/electrical-engineering', methods=['GET', 'POST'])
def ee():
    if 'uname' not in session:
        return redirect(url_for('index'))
    hidden_vals = ee_course['courses']
    doc = user.getCourseDoc(session['uname'], u'electrical-engineering', db)

    if request.method == 'POST':
        user.assignmentCompleted(hidden_vals, session['uname'], u'electrical-engineering', db)
        return redirect(url_for('ee'))

    session['ee'] = user.getProgress(doc, ee_course['courses'])
    return render_template('courses/electroeg.html', doc=doc, ee_course=ee_course['courses'])

# @app.route('/article', methods=['GET', 'POST'])
# def article():                
#     return render_template('courses/article-template.html')

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

        msg = user.create_user(email, password, username, db)
        
        if msg == None:
            doc_ref = db.collection(u'users').document(username)
            doc_ref.set({
                u'uname': username,
            })

            user.setupCourse(session['uname'], u'python', py_course['courses'], db)
            user.setupCourse(session['uname'], u'swift', sw_course['courses'], db)
            user.setupCourse(session['uname'], u'electrical-engineering', ee_course['courses'], db)

            return redirect(url_for('index'))

 
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
        email = request.form.get('email', '', type=str) 
        password = request.form.get('password', '', type=str) 

        msg = user.login_user(email, password)

        if msg != None:
             return render_template( 'accounts/login.html', form=form, msg=msg )
        return redirect(url_for('index'))


    return render_template( 'accounts/login.html', form=form, msg=msg )

# Logout user
@app.route('/logout')
def logout():
    if 'uname' not in session:
        return redirect(url_for('index'))
    user.logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return render_template("pages/error-404.html")



