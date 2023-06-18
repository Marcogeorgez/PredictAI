# ------------------------------------------------WARNING: DONT PRESS Ctrl+S--------------------------------------------
# Importing necessary modules
from datetime import timedelta
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from PredictAI.Key import SECRET_KEY_Value

# Initializing Flask app
app = Flask(__name__, template_folder="html_Files")
# Configuring Flask app
app.config.update(
    TESTING=True,
    SECRET_KEY=SECRET_KEY_Value
)
# Database configuration
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'DESKTOP-329F25T'
DATABASE_NAME = 'StockAI'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}'
# Initializing SQLAlchemy, Bcrypt and LoginManager
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Defining the view function to handle login requests
login_manager.login_view = 'login'
# Setting the login message category
login_manager.login_message_category = "info"
# Setting the cookie duration
login_manager.COOKIE_DURATION = timedelta(days=30)

# Importing the routes module
from PredictAI import Route
