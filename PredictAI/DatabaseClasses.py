from sqlalchemy import VARCHAR, FLOAT, DateTime
from PredictAI import db, login_manager
from flask_login import UserMixin
from datetime import datetime

#  This is a function called load_user that is used in Flask's login_manager to load the user from the database.
#  When a user logs in, their user ID is stored in the session.
#  The load_user function takes the user ID as an argument and returns the corresponding Users object from the database by querying with the ID.
#  This allows Flask to keep track of the current user and their session data.


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# Creating a Users table with columns for id, username, email, password, and datejoined
class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    datejoined = db.Column(db.Date, nullable=False, default=datetime.utcnow)


# Creating a Company table with columns for Symbol, Date, Close_, Adj_Close, and Volume
class Company(db.Model):
    __tablename__ = 'Company'
    Symbol = db.Column(VARCHAR(10), primary_key=True)
    Date = db.Column(DateTime(), primary_key=True)
    Close_ = db.Column(FLOAT(10))
    Adj_Close = db.Column(FLOAT(10))
    Volume = db.Column(FLOAT(10))

    def __init__(self, Symbol, Date, Close_, Adj_Close, Volume):
        self.Symbol = Symbol
        self.Date = Date
        self.Close_ = Close_
        self.Adj_Close = Adj_Close
        self.Volume = Volume


# Creating a company_information table with columns for symbol, Name, Country, IPO_Year, and Sector
class company_information(db.Model):
    __tablename__ = 'company_information'
    symbol = db.Column(VARCHAR(10), primary_key=True)
    Name = db.Column(VARCHAR(20))
    Country = db.Column(VARCHAR(20))
    IPO_Year = db.Column(VARCHAR(20))
    Sector = db.Column(VARCHAR(20))

    def __init__(self, symbol, Name, Country, IPO_Year, Sector):
        self.Symbol = symbol
        self.Name = Name
        self.Country = Country
        self.IPO_Year = IPO_Year
        self.Sector = Sector

# In this code, we are importing the required modules such as VARCHAR, FLOAT, INTEGER, VARBINARY, DateTime, db,
# login_manager, UserMixin, datetime and yfinance. We are then setting up the user loader function for Flask-Login.
# We are creating three tables: Users, Company, and company_information. The Users table has columns for id, username, email,
# password, and datejoined. The Company table has columns for Symbol, Date, Close_, Adj_Close, and Volume.
# The company_information table has columns for symbol, Name, Country, IPO_Year, and Sector.
