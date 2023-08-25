from datetime import timedelta
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from PredictAI.Key import SECRET_KEY_Value

app = Flask(__name__, template_folder="html_Files")
app.config.update(
    TESTING=True,
    SECRET_KEY=SECRET_KEY_Value
)
# Database configuration
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'DESKTOP-HSDSJ4Q\MSSQLSERVER01'
DATABASE_NAME = 'StockAI'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}'

# Initializing SQLAlchemy, Bcrypt and LoginManager
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
login_manager.COOKIE_DURATION = timedelta(days=30)

from PredictAI import Route
