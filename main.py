from flask import (
  Flask, render_template, url_for, flash, redirect, request, session
)
import os
from forms import (
  LoginForm, RegistrationForm,
  CreateAccount, TakeMeThere, Happy, Sad, Bored,
  Content, History
)
from flask_sqlalchemy import SQLAlchemy
import generate
from flask_behind_proxy import FlaskBehindProxy
import datetime
import visual
from datetime import timedelta, datetime
import pandas as pd


IMAGES = os.path.join('static', 'images')
TEMPLATES = os.path.join('Mood-Tracker-Project/templates/')

app = Flask(__name__)

proxied = FlaskBehindProxy(app)

# import secrets secrets.token_hex(16)
app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b'

app.config['UPLOAD_FOLDER'] = IMAGES
app.config['TEMPLATES_FOLDER'] = TEMPLATES


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# alternative -- look into an array to collect mood frequency
db = SQLAlchemy(app)

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
    mood = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        # password field is kept in for testing purposes
        return f"Data('{self.username}', '{self.time}', '{self.mood}', {self.content})"


@app.route("/", methods=['GET', 'POST'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    full_filename2 = os.path.join(
      app.config['UPLOAD_FOLDER'], 'icons/favicon.ico'
    )
    form = LoginForm()
    form2 = CreateAccount()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if not user:
                flash(f'There is no account with this email.')
                return redirect(url_for('login'))
        except Exception:
            flash(f'there is no account with this email.')
            return redirect(url_for('login'))
        else:
            try:
                # user = User.query.filter_by(email=form.email.data).first()
                if user.password != form.password.data:
                    flash(
                      f'the password entered does not match the '
                      'login credentials for the username provided.'
                    )
                    return redirect(url_for('login'))
            except Exception:
                return redirect(url_for('daily'))
            else:
                session['user_name'] = user.username
                username = session['user_name']
                flash(f'hi, {username}!', 'success')
                return redirect(url_for('daily'))
    if form2.validate_on_submit():
        if request.method == 'POST':
            if request.form.get('createaccount') == 'create account':
                return redirect(url_for('createaccount'))
        elif request.method == 'GET':
            return render_template(
              'index.html', image_1=full_filename, favicon=full_filename2,
              form=form, form2=form2
            )
    return render_template(
      'index.html', image_1=full_filename, favicon=full_filename2,
      form=form, form2=form2
    )


@app.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = RegistrationForm()
    full_filename2 = os.path.join(
      app.config['UPLOAD_FOLDER'], 'icons/favicon.ico'
    )
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'img-01.png')
    if form.validate_on_submit():
        user = User(
          username=form.username.data, email=form.email.data,
          password=form.password.data
        )
        checkuser = User.query.filter_by(email=form.email.data).first()
        if checkuser:
            flash(
              f'there is already an account with the email {form.email.data}.',
              'error'
            )
            return redirect(url_for('login'))
    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        flash(
          f'there was an issue with creating your account.',
          'error'
        )
    else:
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template(
      'testaccount.html', favicon=full_filename2, form=form, image_1=full_filename
    )


@app.route("/daily", methods=['GET', 'POST'])
def daily():
    form = Happy()
    form2 = Sad()
    form3 = Bored()
    form4 = History()
    full_filename2 = os.path.join(
      app.config['UPLOAD_FOLDER'], 'icons/favicon.ico'
    )
#     if request.method == 'POST':
#         if request.form.get('generatehappy') == 'generate happy':
#             return redirect(url_for('generate-happy'))
#     elif request.method == 'GET':
#         return render_template(
#           'testdaily.html', favicon=full_filename2, form=form,
#           form2=form2, form3=form3, form4=form4 subtitle="how are you feeling?"
#         )
    return render_template(
      'testdaily.html', favicon=full_filename2, form=form,
      form2=form2, form3=form3, form4=form4, subtitle="how are you feeling?"
    )


@app.route("/generate-happy", methods=['GET', 'POST'])
def happy():
    return generate_content('happy')


@app.route("/generate-sad", methods=['GET', 'POST'])
def sad():
    return generate_content('sad')


@app.route("/generate-bored", methods=['GET', 'POST'])
def bored():
    return generate_content('bored')


def generate_content(mood):
    form = TakeMeThere()
    msg, url, search = generate.generate(mood)
    # msg, url = generate.generate(mood)
    time = datetime.now()
    username = session['user_name']
    data = Data(username=username, time=time, mood=mood, content=search)
    try:
        db.session.add(data)
        db.session.commit()
    except Exception:
        flash(f'There was an error saving your data.', 'error')
    if request.method == 'POST':
        if request.form.get('takemethere') == 'Take me there':
            return redirect(url_for(url))
    elif request.method == 'GET':
        return render_template('generate-mood.html', form=form)
    return render_template(
      'generate-mood.html', subtitle=msg, url=url, form=form
    )


@app.route("/history", methods=['GET', 'POST'])
def history():
    form = Content()
    for document in os.listdir(app.config['TEMPLATES_FOLDER']):
        if document.endswith('graph.html'):
            os.remove(app.config['TEMPLATES_FOLDER'] + document)
    username = session['user_name']
    msg = username + "\'s mood history"
    # make dataframes for graphs
    mood_df_for_timeline = create_mood_df_for_timeline(username)
    mood_df_for_pie = create_mood_df_for_pie(username)
    # make file names for graphs
    filename_tl = os.path.join(
      app.config['TEMPLATES_FOLDER'], 'moodhistorytlgraph.html'
    )
    filename_pie = os.path.join(
      app.config['TEMPLATES_FOLDER'], 'moodhistorypiegraph.html'
    )
    try:
        fig = visual.create_timeline(mood_df_for_timeline, filename_tl)
        fig.update_yaxes(autorange="reversed")
        fig.write_html(filename_tl)
        fig = visual.create_pie(mood_df_for_pie, filename_pie)
        fig.write_html(filename_pie)
    except:
        flash(f'There was an error retrieving your data.', 'error')
        return redirect(url_for('daily'))
    return render_template('history.html', subtitle=msg, form=form)


def create_mood_df_for_timeline(username):
    mood_data = {'Task': [], 'time': [], 'Finish': [], 'mood': [], 'content': []}
    mininc = timedelta(minutes=1)
    window = timedelta(hours=-1)
    now = datetime.now()
    for row in Data.query.filter_by(username=username):
        if row.time > now + window:
            mood_data['Task'].append(row.mood)
            mood_data['mood'].append(row.mood)
            mood_data['time'].append(row.time)
            mood_data['Finish'].append(row.time + mininc)
            mood_data['content'].append(row.content)
    mood_df = pd.DataFrame(mood_data)
    return mood_df
  

def create_mood_df_for_pie(username):
    happy = sad = bored = 0
    mininc = timedelta(minutes=1)
    for row in Data.query.filter_by(username=username):
        mood = row.mood
        if mood == 'happy':
            happy += 1
        if mood == 'sad':
            sad += 1
        if mood == 'bored':
            bored += 1
    mood_data = {'mood': ['happy', 'sad', 'bored'],
                 'num_logs': [happy, sad, bored]
                }
    mood_df = pd.DataFrame(mood_data)
    return mood_df


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
