from flask import Flask, render_template
from flask import send_from_directory
import os


app = Flask(__name__,template_folder="html_Files")


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/aboutus')
def aboutus():
  return render_template('about_us.html')

@app.route('/login')
def login():
  return render_template('Log_sign.html')

@app.route('/prediction')
def stockprediction():
  return render_template('Prediction.html')

@app.route('/stockprices')
def stockprices():
  return render_template('stock_prices.html')

@app.route('/subscription')
def subscription():
  return render_template('Subscription.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='favicon.ico')

if __name__ == '__main__':

  app.run(debug=True)
