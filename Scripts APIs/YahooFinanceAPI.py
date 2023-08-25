import pyodbc
import yfinance as yf

# Server and database details
server = 'DESKTOP-329F25T'
database = 'StockAI'

# Connection details and credentials
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    f'Server={server};'
    f'Database={database};'
    'UID=YOUR_USERNAME;'
    'PWD=YOUR_PASSWORD;'
    'Encrypt=no;'
    'Connection Timeout=30;',
    TrustServerCertificate='yes'
)

# Cursor to execute SQL queries
cursor = conn.cursor()

# Get the last date from the database
cursor.execute('SELECT MAX(Date) FROM Company')
last_date = cursor.fetchone()[0]

# Download the latest stock data for AAPL since the last date in the database
df = yf.download(tickers='AAPL', start=last_date, interval='1d')
ticker = 'AAPL'
# Insert each row of the data frame into the database
for index, row in df.iterrows():
    cursor.execute("INSERT INTO Company (Symbol, Date, Close_, Adj_Close, Volume) VALUES (?, ?, ?, ?, ?)",
                   (ticker, index.date(), row['Close'], row['Adj Close'], row['Volume']))

conn.commit()
