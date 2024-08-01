# PredictAI
# Note to self -> The entire project comments are low-quality made in 6/2023 in a rush when i was novice and starting out.

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
