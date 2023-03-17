import webbrowser


for Ticker in "AAPL ".split():

    webbrowser.open(
        f"https://eodhistoricaldata.com/img/logos/US/{Ticker}.png", autoraise=True)
