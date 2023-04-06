import webbrowser

# insert companies symbol and open the URL in the default browser to be able to download stocks images

for Ticker in "AAPL ".split():

    webbrowser.open(
        f"https://eodhistoricaldata.com/img/logos/US/{Ticker}.png", autoraise=True)
