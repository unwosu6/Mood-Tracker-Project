from flask import Flask, render_template, url_for, flash, redirect, request
import os
from forms import LoginForm

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)
app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b' # import secrets secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = IMAGES

@app.route("/", methods=['GET', 'POST'])
def login():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    form = LoginForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Hi, {form.email.data}!', 'success')
        return redirect(url_for('hello'))
    return render_template('index.html', image_1=full_filename, favicon=full_filename2, form=form)


@app.route("/hello")
def hello():
    return render_template('hello.html', subtitle='Hello Page', text='This is the hello page')


def daily():
    form = Generate() # this does not exist yet
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('hello.html', subtitle='Hello Page', text='This is the hello page', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")