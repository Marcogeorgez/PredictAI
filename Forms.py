from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email , EqualTo

class Registeration(FlaskForm):
    Username    = StringField('Username', validators =[DataRequired(),Length(min=3,max=25)])
    email       = StringField('Email', validators =[DataRequired(),Email()])
    password    = PasswordField('Password',validators =[DataRequired(),Length(min=4,max=30)] )
    Confirmpassword    = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    email       = StringField('Email', validators =[DataRequired(),Email()])
    password    = PasswordField('Password',validators =[DataRequired()] )
    remember    = BooleanField('Remember Me')
    submit      = SubmitField('Login')



    
