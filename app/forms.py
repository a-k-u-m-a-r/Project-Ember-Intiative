# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	email = StringField  (u'Username', validators=[DataRequired()], render_kw={"placeholder": "Email"})
	password = PasswordField(u'Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})

class RegisterForm(FlaskForm):
	username = StringField  (u'Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
	password = PasswordField(u'Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
	email = StringField  (u'Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
