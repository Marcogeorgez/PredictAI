import json
import requests
from bs4 import BeautifulSoup
import datetime
from time import time
start_time = time()
TodayDate = datetime.datetime.now().strftime("%d-%m-%Y")
TodayDateForAPI = datetime.datetime.now().strftime("%Y-%m-%d")
key = "VCQYDMS0XB3D5VBX"
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
    return Company_Symbol ,DateofTrade,Price,Volume


if __name__ == "__main__":
    for symbol in "AAPL ABC AMZN BRK-B CI COST CSV GOOG MCK T UNH WMT XOM".split():
        print(stock_price(f"{symbol}"))
        print("this is a new line \n\n")
    