from PredictAI.key import SECRET_KEY_Value
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import timedelta
from flask_login import LoginManager
app = Flask(__name__,template_folder="html_Files")
app.config.update(
    TESTING=True,
    SECRET_KEY= SECRET_KEY_Value
)

DRIVER_NAME='ODBC Driver 17 for SQL Server'
SERVER_NAME='DESKTOP-329F25T'
DATABASE_NAME='StockAI'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = "info"
login_manager.COOKIE_DURATION = timedelta(days=30)

from PredictAI import Route
