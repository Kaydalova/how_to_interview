import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from interview_app import db, login_manager

from .constants import MAX_TITLE_LENGTH, MAX_TOPIC_LENGTH, MAX_USERNAME_LENGTH


class Topic(db.Model):
    """Модель топиков.
    Attrs:
    - id: уникальный идентификатор конкретного топика
    - name: название топика
    - questions: вопросы, которые относятся к топику - объекты модели Question
    - slug: слаг топика
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(MAX_TOPIC_LENGTH), nullable=False)
    questions = db.relationship('Question', backref='topic', lazy=True)
    slug = db.Column(db.String, unique=True)

    def __repr__(self):
        return self.name


class Question(db.Model):
    """Модель вопросов.
    Attrs:
    - id: уникальный идентификатор вопроса
    - topic_id: id топика, к которому относится вопрос
    - title: заголовок вопроса
    - question: текст вопроса
    - answer: текст ответа
    - user_id: юзер, предложивший вопрос. Может отсутствовать, если вопрос
    был подготовлен админом самостоятельно.
    """
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    title = db.Column(db.String(MAX_TITLE_LENGTH), nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'{self.topic}. {self.question}'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


class User(db.Model, UserMixin):
    """Модель пользователя.
    Attrs:
    - id: уникальный идентификатор пользователя
    - username: юзернейм пользователя, уникальное значение
    - email: почта пользователя, ислоьзуется для отправки
    статуса добавленного вопроса
    - password: пароль
    - created_on: дата создания профиля
    - is_confirmed: подтверждена ли почта
    - confirm_link: уникальная ссылка для подтверждения почты
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(MAX_USERNAME_LENGTH),
        nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    created_on = db.Column(db.Date, default=datetime.date.today)
    is_confirmed = db.Column(db.Boolean, default=False)
    confirm_link = db.Column(db.String(32), unique=True)
    questions = db.relationship(Question)

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
    """Модель статистики повторения вопросов.
    Attrs:
    - id: уникальный идентификатор записи
    - date: дата, за которую была собрана статистика
    - user_id: идентификатор пользователя, для которого собрана статистика
    - solved: количество повторенных вопросов за конкретный день
    """
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    solved = db.Column(db.Integer, default=0)
