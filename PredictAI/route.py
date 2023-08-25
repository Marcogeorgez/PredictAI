
import concurrent
import os
import time
from datetime import date, timedelta

import pandas as pd
import yfinance as yf
from flask import (flash, g, redirect, render_template, request,
                   send_from_directory, url_for)
from flask_login import current_user, login_required, login_user, logout_user
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy import desc

from PredictAI import app, bcrypt, db
from PredictAI.DatabaseClasses import Company, Users, company_information
from PredictAI.Forms import Login, Registeration
from PredictAI.Prediction import PredictFuture
from PredictAI.StockAPIs import CompanyInformation, Stock_Information_Exchange


@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request_time(response):
    diff = time.time() - g.start
    print(f"Page rendered in {diff} seconds")
    return response


@app.route('/home')
@app.route('/')
def index():

    Google = CompanyInformation('GOOGL')
    Microsoft = CompanyInformation('MSFT')
    Apple = CompanyInformation('AAPL')
    Oracle = CompanyInformation('ORCL')

    # get stock info for several companies using multithreading
    companies = ['TSLA', 'INTC',
                 'AMD', 'SBUX', 'V', 'PYPL', 'SONY', 'ADBE']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [CompanyInformation(company) for company in companies]

    list = results

    Egxx = Stock_Information_Exchange('^EGX30CAPPED.CA')
    Egus = Stock_Information_Exchange('EGP=X')
    Gold = Stock_Information_Exchange('GC=F')

    company_information1 = db.session.query(company_information).add_columns(
        company_information.symbol, company_information.Name).all()

    return render_template('index.html', Google=Google, Oracle=Oracle, Apple=Apple, Microsoft=Microsoft,
                           Egxx=Egxx, Egus=Egus, Gold=Gold, list=list, company_information1=company_information1)


@app.route('/aboutus')
def aboutus():
    return render_template('about_us.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = Registeration()
    if form.validate_on_submit():
        # Hash the user's password and add the user to the database
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = Users(username=form.Username.data,
                     email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # Display a success message and redirect to the next page or home page
        flash(f'Account is created for {form.Username.data}', 'success')
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect('/home')
    form2 = Login()
    return render_template('Log_sign.html', form=form, form2=form2)


# This route handles both GET and POST requests for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already authenticated, redirect to home
    if current_user.is_authenticated:
        return redirect('/home')
    form = Registeration()
    form2 = Login()
    # If the form is submitted and validates, check if the user exists and the password is correct
    if form2.validate_on_submit():
        user = Users.query.filter_by(email=form2.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form2.password.data):
            # Log in the user and display a success message
            login_user(user, remember=form2.remember.data)
            flash(f'Account is logged!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect('/home')
        else:
            # Display an error message if the login was unsuccessful
            flash(
                'Unsuccessful Login. Please check your Email and Password, and try again.', 'danger')
    return render_template('Log_sign.html', form2=form2, form=form)


# This route is for the stock prices page where data for several companies is retrieved from Yahoo Finance and displayed using an HTML template
@app.route('/stockprices', methods=['GET', 'POST'])
def currentstock():

    # set the max date to and yesterday's date in db
    maxDate = date(year=2023, month=6, day=16)
    Yesterday = date(year=2023, month=6, day=15)

    # query the database for the top 50 companies with the highest closing stock price on
    comp = db.session.query(Company).filter_by(
        Date=maxDate).order_by(desc(Company.Close_)).limit(50)

    # query the database for all the information about the companies
    company_information1 = db.session.query(company_information).add_columns(
        company_information.symbol, company_information.Name).all()

    # query the database for the closing stock price of the companies 
    x = Company.query.filter_by(Date=maxDate).add_columns(Company.Symbol, Company.Close_)\
        .order_by(desc(Company.Close_)).all()

    # query the database for the closing stock price of the companies 
    y = Company.query.filter_by(Date=Yesterday).add_columns(Company.Symbol, Company.Close_)\
        .order_by(desc(Company.Close_)).all()

    # create a pandas dataframe with the closing stock prices of the companies 
    df1 = pd.DataFrame([(d.Symbol, d.Close_)
                        for d in x], columns=['Symbol', 'Close_'])
    df2 = pd.DataFrame([(d.Symbol, d.Close_)
                        for d in y], columns=['Symbol1', 'Close_1'])
    result = pd.concat([df1, df2], axis=1)

    # calculate the percentage change in stock prices for each company
    result['Percentage'] = ((result['Close_']/result['Close_1'])-1)*100

    # if the request method is POST, get the search_stock_price form data and redirect to the ticker page
    if request.method == 'POST':
        Ticker_Name = request.form.get('search_stock_price').lower()
        if len(Ticker_Name) == 0:
            return redirect('/404')
        return redirect(url_for('ticker', Ticker_Name=Ticker_Name))

    # render the stock_prices.html template with the company data and percentage change in stock prices
    return render_template('stock_prices.html', comp=comp, company_information1=company_information1, result=result)


# This route is for the subscription page
@app.route('/subscription')
def subscription():
    return render_template('Subscription.html')


# This route is for the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='favicon.ico')


# This route is for the 404 error page
@app.route('/404')
def error():
    return render_template('404.html')


# This route is for the help page
@app.route('/Help')
def help():
    return render_template('help.html')


# This route is for the logout page
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# This route is for the account page, which requires authentication
@app.route('/Account')
@login_required
def account():

    return render_template('account.html')


# This route is for the ticker page, which displays information about a specific stock
@app.route('/<Ticker_Name>', methods=['GET', 'POST'])
def ticker(Ticker_Name):
    Symbol = Ticker_Name

    msft = yf.Ticker(f"{Symbol}")
    msft.fast_info
    hist = msft.history(period="2d")

    company_name = Symbol.upper()
    Ticker_Name = Symbol
    PreviousPrice = hist['Close'].values[0]
    CurrentPrice = hist['Close'].values[1]
    PriceChangePercentage = ((CurrentPrice/PreviousPrice)-1)*100
    volume = "{:,}".format(hist['Volume'].values[1])
    Open = hist['Open'].values[1]
    High = hist['High'].values[1]
    Low = hist['Low'].values[1]

    company_information1 = db.session.query(company_information).add_columns(
        company_information.symbol, company_information.Name).all()

    return render_template('Ticker.html', company_name=company_name,
                           Ticker_Name=Ticker_Name, CurrentPrice=CurrentPrice, volume=volume, PriceChangePercentage=PriceChangePercentage,
                           Open=Open, High=High, Low=Low, company_information1=company_information1)


@app.route('/prediction', methods=['GET', 'POST'])
def Stock_Prediction():
    # Setting the maximum date and yesterday's date for filtering data
    maxDate = date(year=2023, month=3, day=8)
    # Retrieve the current page number and number of items per page from the request query parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)

    # Querying the database for companies on alphabetical order on maxDate
    comp_query = db.session.query(Company).filter_by(
        Date=maxDate).order_by(Company.Symbol.asc())

    # Paginate the query results
    comp_paginated = comp_query.paginate(page=page, per_page=per_page)

    # Get the items for the current page
    comp = comp_paginated.items

    # Querying the database for all company information
    company_information1 = db.session.query(company_information).add_columns(
        company_information.symbol, company_information.Name).all()

    # Handling form submission to predict future stock prices
    if request.method == 'POST':
        Ticker_Name = request.form.get('Ticker_Name').lower()
        if len(Ticker_Name) == 0:
            return redirect('/404')
        return redirect(url_for('predictTicker', Ticker_Name=Ticker_Name))

    return render_template('Prediction.html', comp=comp, company_information1=company_information1, pagination=comp_paginated)


@app.route('/Predict_<Ticker_Name>', methods=['GET', 'POST'])
@login_required
def predictTicker(Ticker_Name):
    Symbol = Ticker_Name
    Ticker_Name = Symbol

    # query the database for all the information about the companies
    company_information1 = db.session.query(company_information).add_columns(
        company_information.symbol, company_information.Name).all()

    # Calling the PredictFuture function to predict future stock prices
    x, y = PredictFuture(Ticker_Name)
    z = []
    for i in range(len(x)):
        zx = 'Day {}:'.format(
            (date.today() + timedelta(days=i+1)).strftime('%Y-%m-%d'))
        z.append(zx)

    return render_template('CompanyPrediction.html', Ticker_Name=Ticker_Name, x=x, y=y, z=z, company_information1=company_information1)
