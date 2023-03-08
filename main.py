import datetime
import os
import requests
from key import ApiKey,SECRET_KEY_Value
from flask import Flask, render_template,send_from_directory,flash,redirect,url_for,request
from forms import Registeration, Login
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__,template_folder="html_Files")

app.config.update(
    TESTING=True,
    SECRET_KEY= SECRET_KEY_Value
)

DRIVER_NAME='ODBC Driver 17 for SQL Server'
SERVER_NAME='DESKTOP-HSDSJ4Q'
DATABASE_NAME='Users'
#uid,upd if later added pw&id to db
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql://@{SERVER_NAME}/{DATABASE_NAME}?driver={DRIVER_NAME}'
dbo = SQLAlchemy(app)
bcrypt = Bcrypt(app)




class Users(dbo.Model):
    id = dbo.Column(dbo.Integer, primary_key=True)
    username = dbo.Column(dbo.String(20), unique=True, nullable=False)
    email = dbo.Column(dbo.String(120), unique=True, nullable=False)
    password = dbo.Column(dbo.String(60), nullable=False)




TodayDate = datetime.datetime.now().strftime("%d-%m-%Y")

# TODO how are we going to serve the  data to the user ? after he uses sumbit search button.
#  

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/aboutus')
def aboutus():
  return render_template('about_us.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = Registeration()
    if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user = Users(username=form.Username.data,email=form.email.data,password=hashed_password)
       dbo.session.add(user)
       dbo.session.commit()
       flash(f'Account is created for {form.Username.data}!','success')
       return redirect('/home')           
    form2 = Login()

    return render_template('Log_sign.html',form=form,form2=form2)

@app.route('/login', methods=['GET','POST'])
def login():
    form= Registeration()
    form2 = Login()
    if form2.validate_on_submit():
      flash(f'Account is logged!','success')
      return redirect('/home')

    return render_template('Log_sign.html', form2=form2, form=form )

@app.route('/prediction')
def stockprediction():
  return render_template('Prediction.html')

@app.route('/stockprices')
def stockprices():
  return render_template('stock_prices.html')


@app.route('/stockprices', methods=['GET','POST'])
def temp():
  if request.method == 'POST':
    company_name=request.form.get('search_stock_price')
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={company_name}&apikey={ApiKey}"
    response = requests.get(url)
    data = response.json()
    MetaData = data["Global Quote"]
    Company_Symbol  =   MetaData["01. symbol"]
    OpenPrice  =   MetaData["02. open"]
    HighPrice  =   MetaData["03. high"]
    LowPrice  =   MetaData["04. low"]
    Price  =   MetaData["05. price"]
    Volume  =   MetaData["06. volume"]
    DateofTrade  =   MetaData["07. latest trading day"]
    PreviousClose  =   MetaData["08. previous close"]
    PriceChange  =   MetaData["09. change"]
    PriceChangePercentage  =   MetaData["10. change percent"]

    return redirect('/stockprices',Company_Symbol=Company_Symbol,OpenPrice=OpenPrice,HighPrice=HighPrice,
                    Price=Price,PreviousClose=PreviousClose,DateofTrade=DateofTrade,PriceChange=PriceChange,
                    Volume=Volume,PriceChangePercentage=PriceChangePercentage)
  else:
       return redirect('/home')

@app.route('/subscription')
def subscription():
  return render_template('Subscription.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',mimetype='favicon.ico')

if __name__ == '__main__':
  app.run(debug=True)
