import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler

from .constants import ERROR_SUBJECT, RECEIVER_EMAIL, SENDER_EMAIL

mail_handler = SMTPHandler(
    mailhost='smtp.yandex.ru',
    fromaddr=SENDER_EMAIL,
    toaddrs=RECEIVER_EMAIL,
    subject=ERROR_SUBJECT,
    credentials=(os.getenv('MAIL_USERNAME'), os.getenv('MAIL_PASSWORD')),
    secure=())

mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))


rotating_handler = RotatingFileHandler(
    'logs/how_to_interview.log',
    maxBytes=1_000_000, backupCount=1)
rotating_handler.setLevel(logging.DEBUG)
rotating_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
