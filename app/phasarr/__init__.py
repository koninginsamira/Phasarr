from phasarr.config import Config

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth

from phasarr.helpers.debug import attach_debugpy
from phasarr.helpers.log import init_gunicorn_logging
from phasarr.helpers.database import init_database, migrate_database

from phasarr.variables import is_local, is_dev_environment, is_docker


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
http_auth = HTTPBasicAuth()


init_database(app, db)

if not is_local:
    init_gunicorn_logging(app)

if is_dev_environment:
    if is_local:
        migrate_database(app)
    elif is_docker:
        attach_debugpy(app)


import phasarr.blueprints