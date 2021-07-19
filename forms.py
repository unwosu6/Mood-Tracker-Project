from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from flask_bcrypt import Bcrypt
from flask import Flask
from sitedatabase import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '973ca834e0eda9c6fe6e021a06300d8b'

# for password safety
bcrypt = Bcrypt(app)

class RegistrationForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired()])
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('create account')

# error is not being raised for some reason.
def IsAUserEmail(form, field):
    user = User.query.filter_by(email=field.data).first()
    if not user:
        raise ValidationError('there is no account with this email.')
# problem might be that if the user does not exist, the app will still look 
# for them when validating the password
# to test jusr reomve all validators from line 42
def PasswordCorrect(form, field):
    user = User.query.filter_by(username=form.username.data).first()
    if not bcrypt.check_password_hash(user.password, field.data):
        raise ValidationError('the password entered does not match the login' +
                              ' credentials for the username provided.')


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email(), IsAUserEmail])
    password = PasswordField('password', validators=[InputRequired(), PasswordCorrect])
    submit = SubmitField('login')


class Generate(FlaskForm):
    submit = SubmitField('generate')


class CreateAccount(FlaskForm):
    submit = SubmitField('create account')


class TakeMeThere(FlaskForm):
    submit = SubmitField('take me there')
