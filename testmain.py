from flask import Flask, render_template, url_for, flash, redirect, request
import os

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)
app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b' # import secrets secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = IMAGES

@app.route("/")
@app.route("/hello")
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    return render_template('index.html', image_1=full_filename, favicon=full_filename2)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")