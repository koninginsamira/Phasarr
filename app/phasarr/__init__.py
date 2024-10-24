from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from jinjax import Catalog

from phasarr.classes.config import Config
from phasarr.helpers.debug import attach_debugpy
from phasarr.helpers.log import init_gunicorn_logging
from phasarr.helpers.database import init_database, migrate_database
from phasarr.variables import is_local, is_dev_environment, is_docker, db_path, components_dir, templates_dir


config = Config()

app = Flask(__name__)
app.config["SECRET_KEY"] = config.flask.secret,
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path

catalog = Catalog(jinja_env=app.jinja_env)
catalog.add_folder(components_dir)
catalog.add_folder(templates_dir)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
init_database(app, db)

http_auth = HTTPBasicAuth()

if not is_local:
    init_gunicorn_logging(app)

if is_dev_environment:
    if is_local:
        migrate_database(app)
    elif is_docker:
        attach_debugpy(app)


import phasarr.blueprints