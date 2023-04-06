import os
import requests
from flask import render_template, send_from_directory, flash, redirect, url_for, request
from bs4 import BeautifulSoup
from PredictAI.Forms import Registeration, Login
from PredictAI.key import ApiKey
from PredictAI import app, db, bcrypt
from PredictAI.DatabaseClasses import Users, Companies, Compinfo
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc
import yfinance as yf


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('about_us.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registeration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = Users(username=form.Username.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account is created for {form.Username.data}', 'success')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect('/home')
    form2 = Login()

    return render_template('Log_sign.html', form=form, form2=form2)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/home')
    form = Registeration()
    form2 = Login()
    if form2.validate_on_submit():
        user = Users.query.filter_by(email=form2.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form2.password.data):
            login_user(user, remember=form2.remember.data)
            flash(f'Account is logged!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/home')
        else:
            flash(
                'Unsuccessful Login. Please check your Email and Password, and try again.', 'danger')
    return render_template('Log_sign.html', form2=form2, form=form)


@app.route('/prediction')
def stockprediction():
    return render_template('Prediction.html')


@app.route('/stockprices', methods=['GET', 'POST'])
def currentstock():

    # comp = Companies.query.filter_by(Date <= '2023-3-8').add_columns(CoCompanies.symbol, Companies.close_, Companies.Volume)\
    #     .order_by(desc(Companies.close_)).all()
    maxDate = '2023-03-08'
    LastDay = '2023-03-08'
    Yesterday = '2023-03-07'
    minDate = '2023-03-07'
    comp = db.session.query(Companies).filter(Companies.Date.between(
        minDate, maxDate)).order_by(desc(Companies.Date)).limit(50)
    compinfo = db.session.query(Compinfo).add_columns(
        Compinfo.symbol, Compinfo.Name).all()
    # x = Companies.query.filter_by(Date=LastDay).add_columns(Companies.close_)\
    #     .order_by(desc(Companies.close_)).all()
    # y = Companies.query.filter_by(Date=Yesterday).add_columns(Companies.close_)\
    #     .order_by(desc(Companies.close_)).all()

    if request.method == 'POST':
        Ticker_Name = request.form.get('search_stock_price').lower()
        if len(Ticker_Name) == 0:
            return redirect('/404')
        return redirect(url_for('ticker', Ticker_Name=Ticker_Name))
    return render_template('stock_prices.html', comp=comp, compinfo=compinfo)


@app.route('/subscription')
def subscription():
    return render_template('Subscription.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='favicon.ico')


@app.route('/404')
def error():
    return render_template('404.html')


@app.route('/Help')
def help():
    return render_template('help.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/Account')
@login_required
def account():

    return render_template('account.html')


@app.route('/<Ticker_Name>', methods=['GET', 'POST'])
def ticker(Ticker_Name):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={Ticker_Name}&apikey={ApiKey}"
    response = requests.get(url)
    data = response.json()
    # headers are made to bypass blocking websites
    # (( The User-Agent request header contains a characteristic string that allows the network protocol peers to identify the application type,
    #    operating system, software vendor or software version of the requesting software user agent.
    #     Validating User-Agent header on server side is a common operation so be sure to use valid browser’s User-Agent string to avoid getting blocked.))
    # FOR MORE INFORMATION ->  http://go-colly.org/articles/scraping_related_http_headers/)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    link = f"https://finance.yahoo.com/quote/{Ticker_Name}/"
    ###
    #  This is to get the ticker name -> APPL -> Apple Inc ,etc etc
    ###
    MetaData = data["Global Quote"]
    if len(MetaData) < 2:
        return redirect('/404')

    else:
        response2 = requests.get(link, headers=headers, timeout=5)
        soup = BeautifulSoup(response2.text, "html.parser")
        company_name = soup.find(
            "h1", class_="D(ib) Fz(18px)").get_text(strip=True)
        OpenPrice = MetaData["02. open"]
        HighPrice = MetaData["03. high"]
        LowPrice = MetaData["04. low"]
        Price = MetaData["05. price"]
        Volume = MetaData["06. volume"]
        DateofTrade = MetaData["07. latest trading day"]
        PreviousClose = MetaData["08. previous close"]
        PriceChange = MetaData["09. change"]
        PriceChangePercentage = MetaData["10. change percent"]
        # to make decimals -> 50000000 -> 50,000,000
        volume = f'{int(Volume):,d}'
        return render_template('Ticker.html', company_name=company_name,
                               Ticker_Name=Ticker_Name, Price=Price, volume=volume, DateofTrade=DateofTrade,
                               PriceChangePercentage=PriceChangePercentage)
