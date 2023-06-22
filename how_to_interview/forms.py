from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
    # topic_id
    # title
    # question
    # answer
    # comment