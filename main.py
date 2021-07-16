from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, Generate
from flask_sqlalchemy import SQLAlchemy
import time, random, threading # might remove these imports
from flask_bcrypt import Bcrypt
from sitedatabase import User
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = # must generate

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# for password safety
bcrypt = Bcrypt(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text=gettext('This is the home page'))


@app.route("/daily", methods=['GET', 'POST'])
def daily():
    form = Generate() # this does not exist yet
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('daily.html', subtitle='Hello Page', text='This is the hello page', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():    
    form = LoginForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Hi, {form.username.data}!', 'success')
        return redirect(url_for('captions')) # change to a special page
    return render_template('login.html', subtitle='Login to access your currated feed', form=form)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are validate_on_submit
        # encrypt data
        # password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data) # password_hash)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            flash(f'There is already an account with the username {form.username.data}.', 'error')
        else:
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
    return render_template('signup.html', subtitle='Sign Up', form=form)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")