from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config
from flask_login import LoginManager

from flask_mail import Mail
from flask_admin import Admin
from .admin_views import CustomModelView, SecuredHomeView
from .logging_config import mail_handler, rotating_handler


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
login_manager = LoginManager(app)

mail = Mail(app)

from .models import User, Topic, Question, Statistics # noqa


# -----------------------------------------------------------------------------
# Настройка админ панели.
# -----------------------------------------------------------------------------
admin = Admin(
    app,
    template_mode='bootstrap3',
    index_view=SecuredHomeView(url='/admin'))
admin.add_view(CustomModelView(User, db.session))
admin.add_view(CustomModelView(Topic, db.session))
admin.add_view(CustomModelView(Question, db.session))
admin.add_view(CustomModelView(Statistics, db.session))


from . import cli_commands, views, error_handlers   # noqa


# -----------------------------------------------------------------------------
# Подключение логирования.
# -----------------------------------------------------------------------------
app.logger.addHandler(rotating_handler)

if app.debug:
    app.logger.addHandler(mail_handler)


# SQLite does not support dropping or altering columns.
# However, there is a way to work around this:
# Alembic's batch_alter_table context manager lets you specify
# the changes in a natural way, and does a little
# "make new table - copy data - drop old table - rename new table"
# dance behind the scenes when using SQLite

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
