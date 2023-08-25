# PredictAI

How to use it?
1- Open run.py
2- Run it like a normal python file.
3- Open in chrome or Your browser the Ctrl+lift click to follow http://127.0.0.1:5000/ shown in the terminal.
4- Cancel it by clicking Ctrl+c in the terminal.

What is it built on?
1- Python (Flask)
2- HTML/CSS/JS
3-Microsoft SQL

How to Get stylesheet.css/javascript/image URL with flask?
if the file you want to edit is the .html in html folder.

< link rel="stylesheet" href="{{ url_for('static', filename='stylesheets/style.css') }}" >
< img src="{{url_for('static', filename='Assets/Predict.ai logo White.png')}}" id="logo1" width="220" >
Explanation Is:
Okay, flask can't simply open the image directory in images(or javascript or css stylesheet). it has a default, which is static, so all images have to be stored in statics (for simplicity) to be used.
So, how do we use it?
simply use < img src="{{url_for('static',filename='/images/imag.png')}}" >
what happens is URL for concentrates the static with images so in the end flask reads it like -> static/images/imag.png
