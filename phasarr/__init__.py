import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from jinjax import Catalog

from phasarr.config import PhasarrConfig
from phasarr.helpers.form import is_required
from phasarr.helpers.debug import attach_debugpy
from phasarr.helpers.gunicorn import init_gunicorn_logging, is_gunicorn
from phasarr.helpers.database import init_database, is_upgrade
from phasarr.variables import (
    is_docker,
    components_dir, templates_dir,
    config_path, default_config_path, db_path,
    debug_port
)


app = Flask(__name__)

if is_gunicorn:
    init_gunicorn_logging(app)
    
config = PhasarrConfig(app, path=config_path, default_path=default_config_path)

app.config["SECRET_KEY"] = config.flask.secret
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_path)
app.jinja_env.filters['is_required'] = is_required

catalog = Catalog(jinja_env=app.jinja_env)
catalog.add_folder(components_dir)
catalog.add_folder(templates_dir)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
init_database(app, db)

http_auth = HTTPBasicAuth()
login = LoginManager(app)

if is_docker and app.debug:
    attach_debugpy(app, debug_port)


import phasarr.blueprints