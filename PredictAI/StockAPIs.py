import yfinance as yf
# define a function to extract stock info


def CompanyInformation(Symbol):
    # use yfinance to get stock data
    msft = yf.Ticker(f"{Symbol}")
    # get basic stock info
    msft.fast_info
    # get historical stock data
    hist = msft.history(period="2d")
    # extract relevant information from historical data
    Volume = hist['Volume'].values
    PreviousPrice = hist['Close'].values[0].round(2)
    CurrentPrice = hist['Close'].values[1].round(3)
    PriceChangePercentage = (((CurrentPrice/PreviousPrice)-1)*100).round(2)
    # return the extracted information
    return CurrentPrice, PreviousPrice, PriceChangePercentage, Volume, Symbol


def Stock_Information_Exchange(Symbol):
    # use yfinance to get stock data
    msft = yf.Ticker(f"{Symbol}")
    # get basic stock info
    msft.fast_info
    # get historical stock data
    hist = msft.history(period="2d")
    # extract relevant information from historical data
    PreviousPrice = hist['Open'].values[0].round(2)
    CurrentPrice = hist['Close'].values[0].round(2)
    PriceChangePercentage = (((CurrentPrice/PreviousPrice)-1)*100).round(2)
    # return the extracted information
    return CurrentPrice, PreviousPrice, PriceChangePercentage, Symbol
