from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash

from . import app, db
from .forms import LoginForm, QuestionForm, RegisterForm
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


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('profile_view'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile_view'))
        flash('Неверные учетные данные', 'error')
        return redirect(url_for('login_view'))
    return render_template('login.html', form=form)


@app.route('/profile')
def profile_view():
    print(current_user)
    return render_template('profile.html')


@app.route('/logout/')
@login_required
def logout_view():
    logout_user()
    flash("Вы вышли из профиля.")
    return redirect(url_for('login_view'))
