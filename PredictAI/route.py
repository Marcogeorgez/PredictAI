import os
import requests
from flask import render_template, send_from_directory, flash, redirect, url_for, request
from bs4 import BeautifulSoup
from PredictAI.Forms import Registeration, Login
from PredictAI.key import ApiKey
from PredictAI import app, db, bcrypt
from PredictAI.DatabaseClasses import Users, Company, Compinfo
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import desc
import yfinance as yf
from datetime import date
import pandas as pd
import pyodbc


@app.route('/home')
@app.route('/')
def index():
    def index_company(Symbol):
        msft = yf.Ticker(f"{Symbol}")
        msft.fast_info
        hist = msft.history(period="2d")
        Volume = hist['Volume'].values
        PreviousPrice = hist['Close'].values[0].round(2)
        CurrentPrice = hist['Close'].values[1].round(3)
        PriceChangePercentage = (((CurrentPrice/PreviousPrice)-1)*100).round(2)
        return CurrentPrice, PreviousPrice, PriceChangePercentage, Volume, Symbol
    Google = index_company('GOOGL')
    Microsoft = index_company('MSFT')
    Apple = index_company('AAPL')
    Oracle = index_company('ORCL')
    Adobe = index_company('ADBE')
    AMD = index_company('AMD')
    Amazon = index_company('AMZN')
    Cisco = index_company('CSCO')
    IBM = index_company('IBM')
    Nasdaq = index_company('NDAQ')
    Paypal = index_company('PYPL')
    Sony = index_company('SONY')
    Tesla = index_company('TSLA')
    Uber = index_company('UBER')
    list = [AMD, Adobe, Amazon, Cisco, IBM, Nasdaq, Paypal, Sony, Tesla, Uber]
    compinfo = db.session.query(Compinfo).add_columns(
        Compinfo.symbol, Compinfo.Name).all()

    return render_template('index.html', Google=Google, Oracle=Oracle, Apple=Apple, Microsoft=Microsoft, list=list, compinfo=compinfo)


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
            flash('Login unsucessful. Please check email and password are correct.','danger')
    return render_template('Log_sign.html', form2=form2, form=form )
@app.route('/prediction')
def stockprediction():
  return render_template('Prediction.html')

@app.route('/stockprices', methods=['GET', 'POST'])
def currentstock():

    comp = Companies.query.filter_by(Date='2023-03-08').add_columns(Companies.img,Companies.companyname,Companies.symbol,Companies.close_,Companies.Volume)\
        .order_by(desc(Companies.close_)).all()


    #comp = db.session.execute(db.select(Companies.companyname,Companies.symbol,Companies.close_,Companies.Volume).filter_by(Date='2023-03-08')).order_by(desc(Companies.close_)).all()
    #both are working but first accept order_by , 2nd doesn't.





    if request.method == 'POST':
        Ticker_Name = request.form.get('search_stock_price').lower()
        if len(Ticker_Name) == 0:
            return redirect('/404')
        return redirect(url_for('ticker', Ticker_Name=Ticker_Name))

    return render_template('stock_prices.html', comp=comp, compinfo=compinfo, result=result)


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
    return render_template('Ticker.html', company_name=company_name,
                           Ticker_Name=Ticker_Name, CurrentPrice=CurrentPrice, volume=volume, PriceChangePercentage=PriceChangePercentage
                           )


@app.route('/prediction', methods=['GET', 'POST'])
def stockprediction():

    maxDate = date(year=2023, month=3, day=8)
    Yesterday = date(year=2023, month=3, day=7)

    comp = db.session.query(Company).filter_by(
        Date=maxDate).order_by(desc(Company.Close_)).limit(50)
    compinfo = db.session.query(Compinfo).add_columns(
        Compinfo.symbol, Compinfo.Name).all()
    x = Company.query.filter_by(Date=maxDate).add_columns(Company.Symbol, Company.Close_)\
        .order_by(desc(Company.Close_)).all()
    y = Company.query.filter_by(Date=Yesterday).add_columns(Company.Symbol, Company.Close_)\
        .order_by(desc(Company.Close_)).all()
    df1 = pd.DataFrame([(d.Symbol, d.Close_)
                        for d in x], columns=['Symbol', 'Close_'])
    df2 = pd.DataFrame([(d.Symbol, d.Close_)
                        for d in y], columns=['Symbol1', 'Close_1'])
    result = pd.concat([df1, df2], axis=1)
    result['Percentage'] = ((result['Close_']/result['Close_1'])-1)*100
    if request.method == 'POST':
        Ticker_Name = request.form.get('search_stock_price').lower()
        if len(Ticker_Name) == 0:
            return redirect('/404')
        return redirect(url_for('ticker', Ticker_Name=Ticker_Name))

    return render_template('Prediction.html', comp=comp, compinfo=compinfo, result=result)


