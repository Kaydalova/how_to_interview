from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
mail = Mail(app)

from . import cli_commands, views, error_handlers   # noqa

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
