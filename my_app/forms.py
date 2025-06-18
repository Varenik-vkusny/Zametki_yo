from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators

class AdditionForm(FlaskForm):
    title = StringField('Титл', [validators.DataRequired(), validators.length(min=1, max=120)])
    content = TextAreaField('Контент', [validators.DataRequired(), validators.length(min=1, max=5000)])