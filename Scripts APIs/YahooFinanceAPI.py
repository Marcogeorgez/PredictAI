import pyodbc
import yfinance as yf

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DESKTOP-329F25T'
database = 'StockAI'

# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-329F25T'
                      'Database=StockAI;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

df = yf.download(tickers='AAPL', period='5y', interval='1d')
print(df)

cursor.execute('''
               INSERT INTO Historical_Data' (Date, Open, High, Low, Close, Adj Close, Volume)
               VALUES 
               (df = yf.download(tickers='AAPL', period='5y', interval='1d')
                ''')
conn.commit()


# import yfinance as yf
# from timeit import default_timer as t
# start = t()
# for symbol in "T TSLA AAPL COST AMZN GOOG AMD ABT ABBV A AN".split():
#     msft = yf.Ticker(f"{symbol}")
#     msft.fast_info
#     hist = msft.history(period="1day")
#     print(hist)
# end = t()
# print(end-start)
