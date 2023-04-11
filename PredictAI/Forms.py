from flask_wtf import FlaskForm  # Importing FlaskForm from flask_wtf module
# Importing required form fields
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
# Importing required validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
# Importing the Users class from the PredictAI.DatabaseClasses module
from PredictAI.DatabaseClasses import Users

# Registration form class


class Registeration(FlaskForm):
    # Username field with required validators and a placeholder
    Username = StringField('', validators=[DataRequired(), Length(
        min=3, max=25)], render_kw={"placeholder": "Username"})
    # Email field with required validators and a placeholder
    email = StringField('', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    # Password field with required validators and a placeholder
    password = PasswordField('', validators=[DataRequired(), Length(
        min=4, max=30)], render_kw={"placeholder": "Password"})
    # Confirm password field with required validators and a placeholder
    Confirmpassword = PasswordField('', validators=[DataRequired(), EqualTo(
        'password')], render_kw={"placeholder": "Confirm Password"})
    # Submit button
    submit = SubmitField('Sign Up')

    # Email validation function to check if email already exists
    def validate_email(self, email):
        # Query the Users class to check if email already exists
        email = Users.query.filter_by(email=email.data).first()
        if email:
            # Raise a validation error if email already exists
            raise ValidationError("Email already taken")

# Login form class


class Login(FlaskForm):
    # Email field with required validators and a placeholder
    email = StringField('', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    # Password field with required validators and a placeholder
    password = PasswordField('', validators=[DataRequired()], render_kw={
                             "placeholder": "Password"})
    # Remember me checkbox
    remember = BooleanField('Remember Me')
    # Submit button
    submit = SubmitField('Login')
