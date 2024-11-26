import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, request, url_for
from flask_httpauth import HTTPBasicAuth
from jinjax import Catalog

from phasarr.config import PhasarrConfig
from phasarr.components.form.helpers.form import is_required
from phasarr.components.utilities.helpers.debug import attach_debugpy
from phasarr.components.utilities.helpers.gunicorn import init_gunicorn_logging, is_gunicorn
from phasarr.components.utilities.helpers.database import init_database
from phasarr.variables import (
    is_docker,
    templates_folder,
    config_file, default_config_file, db_file,
    debug_port
)


app = Flask(__name__)

if is_gunicorn:
    init_gunicorn_logging(app)
    
config = PhasarrConfig(app, path=config_file, default_path=default_config_file)
app.config["SECRET_KEY"] = config.flask.secret
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(db_file)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
init_database(app, db)

http_auth = HTTPBasicAuth()
login = LoginManager(app)

if is_docker and app.debug:
    attach_debugpy(app, debug_port)

# ------------------------------------------------------
# Register pages
# ------------------------------------------------------

app.jinja_env.filters['is_required'] = is_required
catalog = Catalog(jinja_env=app.jinja_env)

catalog.add_folder(templates_folder)

from phasarr.components.form import import_component as import_form
from phasarr.components.tree import import_component as import_tree
from phasarr.components.ui import import_component as import_ui
import_form(app, catalog)
import_tree(app, catalog)
import_ui(app, catalog)

from phasarr.auth import auth_app
app.register_blueprint(auth_app, url_prefix="/")
catalog.add_folder(auth_app.template_folder, prefix=auth_app.name)

from phasarr.main import main_app
app.register_blueprint(main_app, url_prefix="/")
catalog.add_folder(main_app.template_folder, prefix=main_app.name)

from phasarr.setup import setup_app, stages
app.register_blueprint(setup_app, url_prefix="/setup")
catalog.add_folder(setup_app.template_folder, prefix=setup_app.name)

from phasarr.api import api_app
app.register_blueprint(api_app, url_prefix="/api")

@app.before_request
def check_setup_stage():
    current_stage = config.setup.stage
    is_blueprint = request.blueprint != None

    is_not_setup = not (request.blueprint == "setup")
    is_not_api = not (request.blueprint == "api")
    is_not_component = request.path.strip("/").split("/")[0] != "fragments"
    is_page = is_not_setup and is_not_api and is_not_component

    setup_is_not_done = not (current_stage > len(stages))

    if (is_blueprint and is_page and setup_is_not_done):
        return redirect(url_for("setup.setup"))