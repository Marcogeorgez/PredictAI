from sqlalchemy import VARCHAR, FLOAT, INTEGER, VARBINARY
from PredictAI import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    datejoined = db.Column(db.Date, nullable=False, default=datetime.utcnow)


class Companies(db.Model):
    __tablename__ = 'Companies'
    symbol = db.Column(VARCHAR(10), primary_key=True)
    Date = db.Column(VARCHAR(20), primary_key=True)
    close_ = db.Column(FLOAT(10))
    Adj_Close = db.Column(FLOAT(10))
    Volume = db.Column(INTEGER)

    def __init__(self, symbol, Date, close_, Adj_Close, Volume):
        self.symbol = symbol
        self.Date = Date
        self.close_ = close_
        self.Adj_Close = Adj_Close
        self.Volume = Volume


class Compinfo(db.Model):
    __tablename__ = 'Compinfo'
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
