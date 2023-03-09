# Predict AI Mans

How to use?
1- Open Main.py
2- Run it like a normal python file.
3- Open in chrome or Your browser the following http://127.0.0.1:5000/

What is it built on ?
1- Flask (Python)
2- HTML/CSS/JS

How to create stylesheet.css/javascript/image with flask?
if the file you want to edit is the .html in html folder.

This IS THE WRONG WAY!! :

< link rel="stylesheet" href="stylesheets/style.css" >
< img src="Assets/Predict.ai logo White.png" id="logo1" width="220" >

THE RIGHT WAY IS!! :

< link rel="stylesheet" href="{{ url_for('static', filename='stylesheets/style.css') }}" >
< img src="{{url_for('static', filename='Assets/Predict.ai logo White.png')}}" id="logo1" width="220" >
Explaination ELI5:
Okey , flask can't simply open the image directory in images(or javascript or css stylesheet). it has a default , which is static, so all images have to be stored in statics (for simplicity) to be used.
So , how do we use it?
simply use < img src="{{url_for('static',filename='/images/imag.png')}}" >
what happens is url for concentrate the static with images so in the end flask reads it like -> static/images/imag.png
