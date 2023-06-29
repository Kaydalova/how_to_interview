from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

from .constants import (MAX_ANSWER_LENGTH, MAX_QUESTION_LENGTH,
                        MAX_TITLE_LENGTH, MAX_TOPIC_LENGTH, MIN_ANSWER_LENGTH,
                        MIN_QUESTION_LENGTH, MIN_TITLE_LENGTH,
                        MIN_TOPIC_LENGTH)


class QuestionForm(FlaskForm):
    topic = StringField(
        'Введите тему вопроса',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_TOPIC_LENGTH, MAX_TOPIC_LENGTH)])
    title = StringField(
        'Введите заголовок вопроса',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_TITLE_LENGTH, MAX_TITLE_LENGTH)])
    question = TextAreaField(
        'Ваш вопрос',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_QUESTION_LENGTH, MAX_QUESTION_LENGTH)])
    answer = TextAreaField(
        'Ответ',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_ANSWER_LENGTH, MAX_ANSWER_LENGTH)])
    submit = SubmitField('Предложить')
