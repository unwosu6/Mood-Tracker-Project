from flask import Flask, render_template, url_for, flash, redirect, request
import os
from forms import LoginForm, RegistrationForm, CreateAccount, TakeMeThere, Happy, Sad, Bored
from flask_sqlalchemy import SQLAlchemy
import generate
from flask_behind_proxy import FlaskBehindProxy
import datetime

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)

proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b' # import secrets secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = IMAGES

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # alternative -- look into an array to collect mood frequency

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        # password field is kept in for testing purposes
        return f"User('{self.username}', '{self.email}', '{self.password}')"

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    mood = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        # password field is kept in for testing purposes
        return f"User('{self.username}', '{self.time}', '{self.mood}')"


@app.route("/login", methods=['GET', 'POST'])
def login():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    form = LoginForm()
    form2 = CreateAccount()
#     try:
#         user = User.query.filter_by(email=form.email.data).first()
#         if not user:
#             flash(f'there is no account with this email.')
#     except:
#         redirect(url_for('login'))
#     else:
#         try:
#             user = User.query.filter_by(email=form.email.data).first()
#             if user.password != form.password.data:
#                 flash(f'the password entered does not match the login credentials for the username provided.')
#         except:
#             redirect(url_for('login'))
#         else:
#             if form.validate_on_submit():
#                 flash(f'Hi, {user.username}!', 'success') # add the code for flash jinja
#                 return redirect(url_for('daily'))
    if request.method == 'POST':
        if request.form.get('createaccount') == 'create account':
            return redirect(url_for('createaccount'))
    elif request.method == 'GET':
        return render_template('testindex.html', image_1=full_filename, favicon=full_filename2, form=form, form2=form2)
    return render_template('testindex.html', image_1=full_filename, favicon=full_filename2, form=form, form2=form2)

@app.route("/", methods=['GET', 'POST'])
@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = RegistrationForm()
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    # print(form.validate_on_submit())
    if form.validate_on_submit(): # checks if entries are validate_on_submit
        user = User(username=form.username.data, email=form.email.data, password=form.password.data) # password_hash)
    # try:
        db.session.add(user)
        db.session.commit()
    # except:
        # flash(f'there is already an account with the email {form.email.data}.', 'error')
    # else:
        # flash(f'Account created for {form.username.data}!', 'success')
        # return redirect(url_for('login'))
    return render_template('testaccount.html', favicon=full_filename2, form=form)


@app.route("/daily", methods=['GET', 'POST'])
def daily():
    form = Happy() # this does not exist yet
    form2 = Sad()
    form3 = Bored()
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    if request.method == 'POST':
        if request.form.get('generatehappy') == 'generate happy':
            return redirect(url_for('generate-happy'))
    elif request.method == 'GET':
        return render_template('generate.html', favicon=full_filename2, form=form, form2=form2, form3=form3, subtitle="how are you feeling?")
    return render_template('generate.html', favicon=full_filename2, form=form, form2=form2, form3=form3, subtitle="how are you feeling?")


@app.route("/generate-happy", methods=['GET', 'POST'])
def happy():
    form = TakeMeThere()
    msg, url = generate.generate('happy')
    if request.method == 'POST':
        if request.form.get('takemethere') == 'take me there':
            return redirect(url_for(url))
    elif request.method == 'GET':
        return render_template('generate-mood.html', form=form)
    return render_template('generate-mood.html', subtitle=msg, url=url, form=form)


@app.route("/generate-sad", methods=['GET', 'POST'])
def sad():
    form = TakeMeThere()
    msg, url = generate.generate('sad')
    if request.method == 'POST':
        if request.form.get('takemethere') == 'take me there':
            return redirect(url)
    elif request.method == 'GET':
        return render_template('generate-mood.html', form=form)
    return render_template('generate-mood.html', subtitle=msg, url=url, form=form)


@app.route("/generate-bored", methods=['GET', 'POST'])
def bored():
    form = TakeMeThere()
    msg, url = generate.generate('bored')
    if request.method == 'POST':
        if request.form.get('takemethere') == 'take me there':
            return redirect(url)
    elif request.method == 'GET':
        return render_template('generate-mood.html', form=form)
    return render_template('generate-mood.html', subtitle=msg, url=url, form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")