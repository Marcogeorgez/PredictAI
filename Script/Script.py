import webbrowser
from datetime import date
d0 = date(1970, 1, 1)
d1 = date.today()

delta = d1 - d0
period2 = (delta.days* 24 * 60* 60)
period1 = period2 - 31536000
for Ticker in "COST AAPL T R".split():
    #period1-period2 = the amount of seconds in 1 year. 3.154e^7 
    # Remember to Update Period1 & Period2.
    # how it works:
    # for every second that passes , the period1,period2 counter is increased by 1.
     # period 2 = date from 1.1.1980 till today in seconds. ( x )
     # period 1 = date from period2 - 3.154e^7 ( y )
     # period 2 - period 1 == get me all DATA from the latest year.
    
    webbrowser.open(f"https://query1.finance.yahoo.com/v7/finance/download/{Ticker}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=true",autoraise=True)