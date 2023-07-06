from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash

from . import app, db
from .constants import EIGHT_WEEKS_DAYS, EMAIL_NOT_CONFIRMED
from .forms import LoginForm, QuestionForm, RegisterForm
from .models import Question, Statistics, Topic, User
from .services import (get_object_by_id, get_random_question,
                       get_topic_by_slug, increase_daily_statistics,
                       send_confirmation, send_new_question,
                       user_set_confirmed)


@app.route('/')
def index_view():
    """
    Главная страница с перечнем доступных топиков.
    """
    topics = Topic.query.all()
    return render_template('topics.html', topics=topics)


@app.route('/<string:slug>')
def questions_view(slug):
    """
    Страница просмотра вопросов конкретного топика.
    """
    topic = get_topic_by_slug(slug)
    if not topic:
        abort(404)
    question = get_random_question(topic)
    if current_user.is_authenticated:
        increase_daily_statistics(current_user.id)
    return render_template('questions.html', question=question, topic=topic)


@app.route('/<int:id>/answer/')
def answer_view(id):
    """
    Страница просмотра ответа на вопрос.
    """
    question = get_object_by_id(id, Question)
    topic = get_object_by_id(question.topic_id, Topic)
    return render_template('answer.html', question=question, topic=topic)


@app.route('/add_question', methods=['GET', 'POST'])
@login_required
def add_question_view():
    """
    Страница с формой для добавления нового вопроса пользователем.
    Если данные из формы валидны - вопрос отправляется
    в чат тг для ручной модерации.
    """
    if not current_user.is_confirmed:
        flash(EMAIL_NOT_CONFIRMED, 'confirmation_required')
    form = QuestionForm()
    if form.validate_on_submit():
        send_new_question(form)
        return redirect(url_for('add_success_view'))
    return render_template('add_question.html', form=form)


@app.route('/add_success')
def add_success_view():
    """
    Страница успешного добавления вопроса.
    """
    return render_template('add_success.html')


@app.route('/register', methods=['GET', 'POST'])
def register_view():
    """
    Страница с формой регистрации.
    Если форма валидна создается пользователь
    и происходит редирект в профиль пользователя.
    """
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
        send_confirmation(user)
        return redirect(url_for('profile_view'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_view():
    """
    Страница авторизации пользователя.
    """
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
@login_required
def profile_view():
    """
    Профиль пользователя.
    """
    statistics = Statistics.query.filter_by(
        user_id=current_user.id).order_by(
            Statistics.date).all()
    if len(statistics) < EIGHT_WEEKS_DAYS:
        longer = [Statistics(solved=0)] * (EIGHT_WEEKS_DAYS-len(statistics))
        statistics = longer + statistics
    return render_template('profile.html', statistics=statistics)


@app.route('/logout/')
@login_required
def logout_view():
    """
    Выход из профиля и редирект на страницу авторизации.
    """
    logout_user()
    flash('Вы вышли из профиля.')
    return redirect(url_for('login_view'))


@app.route('/confirm/<string:link>/')
def confirm_email_view(link):
    """
    Проверка уникальной ссылки подтверждения почты и редирект в профиль.
    """
    user_set_confirmed(link)
    flash('Почта успешно подтверждена.', 'email_confirmed')
    return redirect(url_for('profile_view'))
