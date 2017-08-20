from flask_wtf import FlaskForm
from wtforms import TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class MessageForm(FlaskForm):
    title = TextField('Title', validators=[DataRequired(), Length(min=6, max=40)])
    description = TextField('Description', validators={DataRequired(), Length(max=140)})