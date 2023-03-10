from PredictAI.key import SECRET_KEY_Value
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__,template_folder="html_Files")
app.config.update(
    TESTING=True,
    SECRET_KEY= SECRET_KEY_Value
)
DRIVER_NAME='ODBC Driver 17 for SQL Server'
SERVER_NAME='DESKTOP-HSDSJ4Q'
DATABASE_NAME='Users'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from PredictAI import route