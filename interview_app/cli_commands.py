import csv

import click

from . import app, db
from .models import Topic, Question


@app.cli.command('load_topics')
def load_topics_command():
    """Функция загрузки топиков в базу данных."""
    with open('topics.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Topic(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено топиков: {counter}')


@app.cli.command('load_questions')
def load_questions_command():
    """Функция загрузки вопросов в базу данных."""
    with open('questions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            opinion = Question(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено вопросов: {counter}')