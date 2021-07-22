from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
  DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
)
from flask import Flask


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField(
      'confirm password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('create account')


class LoginForm(FlaskForm):
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('login')


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


class History(FlaskForm):
    submit = SubmitField('history')


class Content(FlaskForm):
    submit = SubmitField('back to content')
