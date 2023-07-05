import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'alexandrakaydalova@yandex.ru'  
    MAIL_DEFAULT_SENDER = 'alexandrakaydalova@yandex.ru'  
    MAIL_PASSWORD = 'ulblwisalzobfudd'
