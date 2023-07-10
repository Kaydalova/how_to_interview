MIN_TOPIC_LENGTH = 2
MAX_TOPIC_LENGTH = 20

MIN_TITLE_LENGTH = 5
MAX_TITLE_LENGTH = 50

MIN_QUESTION_LENGTH = 20
MAX_QUESTION_LENGTH = 500

MIN_ANSWER_LENGTH = 2
MAX_ANSWER_LENGTH = 200

MAX_USERNAME_LENGTH = 30

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 16


# validating messages
DATA_REQUIRED = 'Обязательное поле'
PASSWORD_LENGTH = 'Пароль должен быть от 8 до 16 символов'
WRONG_USERNAME = 'Username должен содержать только буквы и цифры'
EIGHT_WEEKS_DAYS = 56


# email confirmation
SUBJECT = 'Подтверждение почты'
MAIN_URL = 'http://127.0.0.1:5000/confirm/'
CONFIRM_MESSAGE = '''
Вы получили это сообщение так как прошли регистрацию на сервисе How to interview.
После завершения регистрации и подтверждения почты вам будет доступно добавление своего вопроса.
Для подтверждения регистрации перейдите по ссылке {}.'''
SENDER_EMAIL = 'alexandrakaydalova@yandex.ru'
EMAIL_NOT_CONFIRMED = 'Добавление вопроса станет доступно после подтверждения почты'


# data files
QUESTIONS_CSV = 'interview_app/static/data/questions.csv'
TOPICS_CSV = 'interview_app/static/data/topics.csv'

# logging constants
RECEIVER_EMAIL = 'alexandrakaydalova95@gmail.com'
ERROR_SUBJECT = 'Ошибка в работе How to interview'

# logging messages
NEW_USER = 'Зарегистрирован новый пользователь - {}'
NEW_QUESTION = '{} предложил новый вопрос'
CONFIRMATION_SENT = '{} отправлено письмо для подтверждения почты'
EMAIL_CONFIRMED = 'Почта {} успешно подтверждена.'
