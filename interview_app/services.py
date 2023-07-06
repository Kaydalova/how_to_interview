import datetime
import os
import uuid
from random import randrange
from urllib.parse import urljoin

from dotenv import load_dotenv
from flask import abort
from flask_mail import Message
from telegram import Bot

from . import db, mail
from .constants import CONFIRM_MESSAGE, MAIN_URL, SENDER_EMAIL, SUBJECT
from .models import Question, Statistics, Topic, User

load_dotenv()


def get_topic_by_slug(slug):
    """
    Функция возвращает объект класса Topic по его slug.
    """
    topic = Topic.query.filter_by(slug=slug).first()
    return topic


def get_object_by_id(id, model):
    """
    Функция возвращает объект указанной модели по еe id.
    """
    object = model.query.filter_by(id=id).first()
    return object


def get_random_question(topic):
    """
    Функция возвращает рандомный вопрос из базы по указанному топику.
    """
    quantity = Question.query.filter_by(
        topic_id=topic.id).count()
    if not quantity:
        abort(404)
    offset_value = randrange(quantity)
    question = Question.query.filter_by(
        topic_id=topic.id).offset(offset_value).first()
    return question


def send_new_question(form):
    """
    Функция отправляет новый вопрос, который предложил пользователь,
    администратору в Телеграм.
    """
    bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
    text = f'''Новый вопрос по теме {form.data.get('topic')}:
Заголовок: {form.data.get('title')}
Вопрос: {form.data.get('question')}
Ответ: {form.data.get('answer')}
'''
    bot.send_message(os.getenv('TELEGRAM_CHAT_ID'), text=text)


def increase_daily_statistics(user_id):
    """
    Функция создает новую запись модели Statistics, если ее еще нет
    и увеличивает счетчик просмотра вопросов на 1 при каждом вызове.
    """
    today = datetime.date.today()
    today_statistics = Statistics.query.filter_by(
        user_id=user_id, date=today).first()
    if not today_statistics:
        today_statistics = Statistics(
            date=today, user_id=user_id, solved=1)
        db.session.add(today_statistics)
        db.session.commit()
    else:
        today_statistics.solved += 1
        db.session.add(today_statistics)
        db.session.commit()


def send_confirmation(user):
    """
    Функция отправляет на почту пользователя ссылку
    для подтверждения почты.
    """
    confirmation_uuid = uuid.uuid4()
    confirm_link = urljoin(MAIN_URL, f'{confirmation_uuid}/')
    user.confirm_link = str(confirmation_uuid)
    db.session.add(user)
    db.session.commit()

    msg = Message(SUBJECT,
                  sender=SENDER_EMAIL,
                  recipients=[user.email])
    msg.body = CONFIRM_MESSAGE.format(confirm_link)
    mail.send(msg)


def user_set_confirmed(link):
    """
    Функция проверяет наличие в базе пользователя с указанной
    ссылкой для подтверждения.
    Если пользователь найден - полю is_confirmed присваивается значение True,
    а уникальная ссылка для подтверждения удаляется.
    Если нет - поднимает ошибку 404.
    """
    user = User.query.filter_by(confirm_link=link).first()
    if not user:
        abort(404)
    user.is_confirmed = True
    user.confirm_link = None
    db.session.add(user)
    db.session.commit()
