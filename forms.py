from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
# from flask_bcrypt import Bcrypt
from flask import Flask

class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('create account')

# error is not being raised for some reason.
# def IsAUserEmail(form, field):
#     user = User.query.filter_by(email=field.data).first()
#     if not user:
#         raise ValidationError('there is no account with this email.')
# problem might be that if the user does not exist, the app will still look 
# for them when validating the password
# to test jusr reomve all validators from line 42
# def PasswordCorrect(form, field):
#     user = User.query.filter_by(username=form.username.data).first()
#     if not bcrypt.check_password_hash(user.password, field.data):
#         raise ValidationError('the password entered does not match the login' +
#                               ' credentials for the username provided.')


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('login')


# class Generate(FlaskForm):
#     submit = SubmitField('generate')


class CreateAccount(FlaskForm):
    submit = SubmitField('create account')


class TakeMeThere(FlaskForm):
    submit = SubmitField('take me there')


class Happy(FlaskForm):
    submit = SubmitField('happy :)')

class Sad(FlaskForm):
    submit = SubmitField('sad :(')

class Bored(FlaskForm):
    submit = SubmitField('bored :/')
