from sqlalchemy import VARCHAR,text
from PredictAI import db,login_manager
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
    datejoined = db.Column(db.Date,nullable=False,default = datetime.utcnow)
class Companies(db.Model):
    __tablename__ = 'Companies'    
    symbol      = db.Column(VARCHAR, primary_key=True) 
    companyname = db.Column(VARCHAR,) 
    Date        = db.Column(VARCHAR, primary_key=True) 
    close_      = db.Column(VARCHAR) 
    Adj_Close   = db.Column(VARCHAR) 
    Volume      = db.Column(VARCHAR) 
    def __init__(self,symbol,companyname,Date,close_,Adj_Close,Volume):
        self.symbol= symbol
        self.companyname=companyname
        self.Date=Date
        self.close_=close_
        self.Adj_Close=Adj_Close
        self.Volume=Volume
    




