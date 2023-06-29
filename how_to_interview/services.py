import os
from random import randrange

from dotenv import load_dotenv
from telegram import Bot

from .models import Question, Topic

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
    if quantity:
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
