import datetime
import os
import requests
from key import ApiKey,SECRET_KEY_Value
from flask import Flask, render_template,send_from_directory,flash,redirect,url_for,request
from Forms import Registeration, Login
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from bs4 import BeautifulSoup



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
      Ticker_Name = request.form.get('search_stock_price').lower()
      if len(Ticker_Name) == 0:
        return redirect('/404')
      return redirect(url_for('noidea',Ticker_Name=Ticker_Name))
  else:
     pass

@app.route('/<Ticker_Name>',methods=['GET', 'POST'])
def noidea(Ticker_Name):
  url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={Ticker_Name}&apikey={ApiKey}"
  response = requests.get(url)
  data = response.json()
  # headers are made to bypass blocking websites
  # (( The User-Agent request header contains a characteristic string that allows the network protocol peers to identify the application type,
  #    operating system, software vendor or software version of the requesting software user agent.
  #     Validating User-Agent header on server side is a common operation so be sure to use valid browser’s User-Agent string to avoid getting blocked.))
  # FOR MORE INFORMATION ->  http://go-colly.org/articles/scraping_related_http_headers/)
  headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36' } 
  link = f"https://finance.yahoo.com/quote/{Ticker_Name}/"
  ###
  #  This is to get the ticker name -> APPL -> Apple Inc ,etc etc
  response2 = requests.get(link, headers=headers, timeout=5)
  soup = BeautifulSoup(response2.text, "html.parser")
  company_name     = soup.find("h1", class_="D(ib) Fz(18px)").get_text(strip=True)
  ###
  MetaData = data["Global Quote"]
  if len(MetaData) < 2 :
    return redirect('/404')

  else:          
    OpenPrice  =   MetaData["02. open"]
    HighPrice  =   MetaData["03. high"]
    LowPrice  =   MetaData["04. low"]
    Price  =   MetaData["05. price"]
    Volume  =   MetaData["06. volume"]
    DateofTrade  =   MetaData["07. latest trading day"]
    PreviousClose  =   MetaData["08. previous close"]
    PriceChange  =   MetaData["09. change"]
    PriceChangePercentage  =   MetaData["10. change percent"]
    volume = f'{int(Volume):,d}' #to make decimals -> 50000000 -> 50,000,000
    

    return render_template('Ticker.html',company_name=company_name,
    Ticker_Name=Ticker_Name,Price=Price, volume=volume,DateofTrade=DateofTrade,
    PriceChangePercentage=PriceChangePercentage)
  

@app.route('/subscription')
def subscription():
  return render_template('Subscription.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='favicon.ico')

@app.route('/404')
def error():
   return render_template('404.html')

@app.route('/Help')
def help():
   return render_template('help.html')
if __name__ == '__main__':
  app.run(debug=True)
