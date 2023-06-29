from flask import flash, redirect, render_template, url_for
from flask_login import login_user

from . import app
from .forms import LoginForm, QuestionForm
from .models import Question, Topic, User
from .services import (get_object_by_id, get_random_question,
                       get_topic_by_slug, send_new_question)


@app.route('/')
def index_view():
    topics = Topic.query.all()
    return render_template('topics.html', topics=topics)


@app.route('/<string:slug>')
def questions_view(slug):
    topic = get_topic_by_slug(slug)
    question = get_random_question(topic)
    return render_template('questions.html', question=question, topic=topic)


@app.route('/<int:id>/answer/')
def answer_view(id):
    question = get_object_by_id(id, Question)
    topic = get_object_by_id(question.topic_id, Topic)
    return render_template('answer.html', question=question, topic=topic)


@app.route('/add_question', methods=['GET', 'POST'])
def add_question_view():
    """
    Функция для отправки формы с новым запросом.
    Если данные из формы валидны - вопрос отправляется
    в чат тг для ручной модерации.
    """
    form = QuestionForm()
    if form.validate_on_submit():
        send_new_question(form)
        return redirect(url_for('add_success_view'))
    return render_template('add_question.html', form=form)


@app.route('/add_success')
def add_success_view():
    return render_template('add_success.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_user_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('users_view'))
        flash('Неверные учетные данные', 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)
