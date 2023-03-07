import datetime
import os
import requests
from key import key
from flask import Flask, render_template,send_from_directory

app = Flask(__name__,template_folder="html_Files")

TodayDate = datetime.datetime.now().strftime("%d-%m-%Y")

# TODO how are we going to serve the  data to the user ? after he uses sumbit search button.
#  
def stock_price(CompanySymbol: str = "AAPL") -> str:
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={CompanySymbol}&apikey={key}"
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
    return DateofTrade,Company_Symbol , OpenPrice , HighPrice, LowPrice,Price,Volume,PriceChange,PriceChangePercentage

@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/aboutus')
def aboutus():
  return render_template('about_us.html')

@app.route('/login')
def login():
  return render_template('Log_sign.html')

@app.route('/prediction')
def stockprediction():
  return render_template('Prediction.html')

@app.route('/stockprices')
def stockprices():
  return render_template('stock_prices.html')

@app.route('/subscription')
def subscription():
  return render_template('Subscription.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',mimetype='favicon.ico')

if __name__ == '__main__':
  app.run(debug=True)
