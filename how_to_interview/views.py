from . import app
from .models import Topic, Question
from flask import render_template
from random import randrange


def get_random_question(id):
    quantity = Question.query.filter_by(topic_id=id).count()
    if quantity:
        offset_value = randrange(quantity)
        question = Question.query.filter_by(topic_id=id).offset(offset_value).first()
        return question


@app.route('/')
def index_view():
    topics = Topic.query.all()
    return render_template('topics.html', topics=topics)


@app.route('/<int:id>')
def questions_view(id):
    question =  get_random_question(id)
    return render_template('questions.html', question=question)