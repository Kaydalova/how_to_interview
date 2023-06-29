from how_to_interview import db

from .constants import MAX_TITLE_LENGTH, MAX_TOPIC_LENGTH


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_TOPIC_LENGTH), nullable=False)
    questions = db.relationship('Question', backref='topic', lazy=True)
    slug = db.Column(db.String, unique=True)

    def __repr__(self):
        return self.name


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    title = db.Column(db.String(MAX_TITLE_LENGTH), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.topic} - {self.title}'
