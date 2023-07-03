import csv

import click

from . import app, db
from .models import Topic, Question

@app.cli.command('create_db')
def create_database():
    """Функция создания базы данных."""
    db.drop_all()
    db.create_all()
    db.session.commit()
    click.echo('База данных создана')


def load_topics():
    """Функция загрузки топиков в базу данных."""
    with open('interview_app/static/data/topics.csv', encoding='utf-8-sig') as f:
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
    load_topics()
    with open('interview_app/static/data/questions.csv', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter=';')
        counter = 0
        for row in reader:
            row['answer']=row['answer'].replace('\n', '<br>')
            opinion = Question(**row)
            db.session.add(opinion)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено вопросов: {counter}')

