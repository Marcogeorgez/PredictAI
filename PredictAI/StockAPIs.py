import yfinance as yf


def CompanyInformation(Symbol):
    # use yfinance to get stock data
    msft = yf.Ticker(f"{Symbol}")
    msft.fast_info
    hist = msft.history(period="2d")
    Volume = hist['Volume'].values
    PreviousPrice = hist['Close'].values[0].round(2)
    CurrentPrice = hist['Close'].values[1].round(3)
    PriceChangePercentage = (((CurrentPrice/PreviousPrice)-1)*100).round(2)
    return CurrentPrice, PreviousPrice, PriceChangePercentage, Volume, Symbol


def Stock_Information_Exchange(Symbol):
    msft = yf.Ticker(f"{Symbol}")
    msft.fast_info
    hist = msft.history(period="2d")
    PreviousPrice = hist['Open'].values[0].round(2)
    CurrentPrice = hist['Close'].values[0].round(2)
    PriceChangePercentage = (((CurrentPrice/PreviousPrice)-1)*100).round(2)
    return CurrentPrice, PreviousPrice, PriceChangePercentage, Symbol
