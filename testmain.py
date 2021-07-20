from flask import Flask, render_template, url_for, flash, redirect, request
import os
from forms import LoginForm, Generate, RegistrationForm, CreateAccount
from flask_sqlalchemy import SQLAlchemy
from sitedatabase import User
import generate
from flask_behind_proxy import FlaskBehindProxy

IMAGES = os.path.join('static', 'images')

app = Flask(__name__)

proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b' # import secrets secrets.token_hex(16)

app.config['UPLOAD_FOLDER'] = IMAGES

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    form = LoginForm()
    form2 = CreateAccount()
    if form2.validate_on_submit():
        return redirect(url_for('createaccount'))
    if form.validate_on_submit():
        # password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(f'Hi, {form.name.data}!', 'success')
        return redirect(url_for('daily'))
    return render_template('testindex.html', image_1=full_filename, favicon=full_filename2, form=form, form2=form2)


@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = RegistrationForm()
    full_filename2 = os.path.join(app.config['UPLOAD_FOLDER'], 'icons/favicon.ico')
    if form.validate_on_submit(): # checks if entries are validate_on_submit
        # encrypt data
        # password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=form.password.data) # password_hash)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            flash(f'There is already an account with the email {form.email.data}.', 'error')
        else:
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('testaccount.html', favicon=full_filename2, form=form)


@app.route("/daily", methods=['GET', 'POST'])
def daily():
    form = Generate() # this does not exist yet
    # how do we get the user entered emotion?
    if form.validate_on_submit():
        return redirect(url_for('generate-happy'))
    return render_template('hello.html', subtitle='Hello Page', text='This is the hello page', form=form)


@app.route("/generate-happy")
def happy():
    msg, url = generate.generate('happy')
    return render_template('generate.html', subtitle=msg, text=url)
    # return render_template('generate.html')


@app.route("/generate-sad")
def sad():
    return render_template('hello.html', subtitle='Sad Page', text='This is the sad page')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")