from . import app
from .models import Topic, Question
from flask import render_template
from random import randrange


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
    return render_template('answer.html', question=question, slug=topic.slug)


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
