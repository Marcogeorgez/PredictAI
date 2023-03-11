from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField,ValidationError
from wtforms.validators import DataRequired, Length, Email , EqualTo
from PredictAI.DatabaseClasses import Users

class Registeration(FlaskForm):
    Username            = StringField('Username', validators =[DataRequired(),Length(min=3,max=25)])
    email               = StringField('Email', validators =[DataRequired(),Email()])
    password            = PasswordField('Password',validators =[DataRequired(),Length(min=4,max=30)] )
    Confirmpassword     = PasswordField('Confirm Password',validators =[DataRequired(),EqualTo('password')])
    submit              = SubmitField('Sign Up')
    def validate_email(self, email):
        email = Users.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already taken, choose another one.")

class Login(FlaskForm):
    email               = StringField('Email', validators =[DataRequired(),Email()])
    password            = PasswordField('Password',validators =[DataRequired()] )
    remember            = BooleanField('Remember Me')
    submit              = SubmitField('Login')



    
