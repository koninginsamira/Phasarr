from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from jinjax import Catalog

from phasarr.config import PhasarrConfig
from phasarr.helpers.form import is_required
from phasarr.helpers.debug import attach_debugpy
from phasarr.helpers.log import init_gunicorn_logging
from phasarr.helpers.database import init_database, migrate_database
from phasarr.variables import (
    is_local, is_dev_environment, is_docker,
    components_dir, templates_dir, migrations_dir,
    db_path, config_path, default_config_path
)


app = Flask(__name__)
config = PhasarrConfig(app, path=config_path, default_path=default_config_path)

app.config["SECRET_KEY"] = config.flask.secret,
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.jinja_env.filters['is_required'] = is_required

catalog = Catalog(jinja_env=app.jinja_env)
catalog.add_folder(components_dir)
catalog.add_folder(templates_dir)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
init_database(app, db)

http_auth = HTTPBasicAuth()
login = LoginManager(app)

if not is_local:
    init_gunicorn_logging(app)

if is_dev_environment:
    if is_local:
        migrate_database(app, migrations_dir)
    elif is_docker:
        attach_debugpy(app)


import phasarr.blueprints