from flask_wtf import  FlaskForm
from wtforms import StringField , PasswordField, SubmitField, BooleanField,ValidationError
from wtforms.validators import DataRequired, Length, Email , EqualTo
from PredictAI.DatabaseClasses import Users

class Registeration(FlaskForm):
    Username            = StringField('', validators =[DataRequired(),Length(min=3,max=25)], render_kw={"placeholder" : "Username"})
    email               = StringField('', validators =[DataRequired(),Email()], render_kw={"placeholder" : "Email"})
    password            = PasswordField('',validators =[DataRequired(),Length(min=4,max=30)], render_kw={"placeholder" : "Password"} )
    Confirmpassword     = PasswordField('',validators =[DataRequired(),EqualTo('password')], render_kw={"placeholder" : "Confirm Password"})
    submit              = SubmitField('Sign Up')
    def validate_email(self, email):
        email = Users.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already taken")

class Login(FlaskForm):
    email               = StringField('', validators =[DataRequired(),Email()], render_kw={"placeholder" : "Email"})
    password            = PasswordField('',validators =[DataRequired()], render_kw={"placeholder" : "Password"}  )
    remember            = BooleanField('Remember Me')
    submit              = SubmitField('Login')


    
