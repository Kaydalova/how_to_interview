import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    # MAIL_SERVER
    # MAIL_PORT
    # MAIL_USE_TLS
    # MAIL_USERNAME
    # MAIL_DEFAULT_SENDER
    # MAIL_PASSWORD


