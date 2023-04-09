from sqlalchemy import VARCHAR,FLOAT,INTEGER,VARBINARY
from PredictAI import db,login_manager
from flask_login import UserMixin
from datetime import datetime
# This is a function called load_user that is used in Flask's login_manager to load the user from the database.
#  When a user logs in, their user ID is stored in the session.
#  The load_user function takes the user ID as an argument and returns the corresponding Users object from the database by querying with the ID.
#  This allows Flask to keep track of the current user and their session data.
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
    symbol      = db.Column(VARCHAR(10), primary_key=True) 
    companyname = db.Column(VARCHAR(50),) 
    Date        = db.Column(VARCHAR(10), primary_key=True) 
    close_      = db.Column(FLOAT(10)) 
    Adj_Close   = db.Column(FLOAT(10)) 
    Volume      = db.Column(INTEGER)
    img         = db.Column(VARCHAR)
    def __init__(self,symbol,companyname,Date,close_,Adj_Close,Volume,img):
        self.symbol= symbol
        self.companyname=companyname
        self.Date=Date
        self.close_=close_
        self.Adj_Close=Adj_Close
        self.Volume=Volume
        self.img=img
    




