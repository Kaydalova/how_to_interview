import datetime

from flask_login import UserMixin
from how_to_interview import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash

from .constants import MAX_TITLE_LENGTH, MAX_TOPIC_LENGTH, MAX_USERNAME_LENGTH


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


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(MAX_USERNAME_LENGTH),
        nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'{self.id} - {self.username}'

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    solved = db.Column(db.Integer, default=0)
