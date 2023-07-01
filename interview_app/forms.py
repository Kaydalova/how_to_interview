from flask_wtf import FlaskForm
from wtforms import (BooleanField, EmailField, PasswordField, StringField,
                     SubmitField, TextAreaField)
from wtforms.validators import DataRequired, Email, Length, Regexp

from .constants import (DATA_REQUIRED, MAX_ANSWER_LENGTH, MAX_PASSWORD_LENGTH,
                        MAX_QUESTION_LENGTH, MAX_TITLE_LENGTH,
                        MAX_TOPIC_LENGTH, MIN_ANSWER_LENGTH,
                        MIN_PASSWORD_LENGTH, MIN_QUESTION_LENGTH,
                        MIN_TITLE_LENGTH, MIN_TOPIC_LENGTH, PASSWORD_LENGTH,
                        WRONG_USERNAME)


class QuestionForm(FlaskForm):
    topic = StringField(
        'Введите тему вопроса',
        validators=[DataRequired(message=DATA_REQUIRED),
                    Length(MIN_TOPIC_LENGTH, MAX_TOPIC_LENGTH)])
    title = StringField(
        'Введите заголовок вопроса',
        validators=[DataRequired(message=DATA_REQUIRED),
                    Length(MIN_TITLE_LENGTH, MAX_TITLE_LENGTH)])
    question = TextAreaField(
        'Ваш вопрос',
        validators=[DataRequired(message=DATA_REQUIRED),
                    Length(MIN_QUESTION_LENGTH, MAX_QUESTION_LENGTH)])
    answer = TextAreaField(
        'Ответ',
        validators=[DataRequired(message=DATA_REQUIRED),
                    Length(MIN_ANSWER_LENGTH, MAX_ANSWER_LENGTH)])
    submit = SubmitField('Предложить')


class RegisterForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(message=DATA_REQUIRED),
            Regexp(regex=r'[а-яА-ЯёЁa-zA-Z0-9]+', message=WRONG_USERNAME)])
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message=DATA_REQUIRED),
            Email(message='Проверьте введенный email')])
    password = PasswordField(
        'Пароль',
        validators=[
            DataRequired(message=DATA_REQUIRED),
            Length(
                MIN_PASSWORD_LENGTH,
                MAX_PASSWORD_LENGTH,
                message=PASSWORD_LENGTH)])
    submit = SubmitField(
        'Регистрация')


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(message=DATA_REQUIRED)])
    password = PasswordField(
        'Пароль',
        validators=[DataRequired(message=DATA_REQUIRED)])
    remember = BooleanField(
        'Запомнить меня')
    submit = SubmitField(
        'Войти')
