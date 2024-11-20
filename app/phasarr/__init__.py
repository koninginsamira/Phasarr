from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from jinjax import Catalog

from phasarr.config import PhasarrConfig
from phasarr.helpers.form import is_required
from phasarr.helpers.debug import attach_debugpy
from phasarr.helpers.database import init_database, migrate_database
from phasarr.variables import (
    is_dev_environment, is_docker,
    components_dir, templates_dir, migrations_dir,
    db_path, config_path, default_config_path
)


config = PhasarrConfig(path=config_path, default_path=default_config_path)
catalog = Catalog()
db = SQLAlchemy()
migrate = Migrate()
http_auth = HTTPBasicAuth()
login = LoginManager()
# login.login_view = 'auth.login'
# login.login_message = _l('Please log in to access this page.')

def create_app():
    app = Flask(__name__)
    config.init_app(app)

    app.config["SECRET_KEY"] = config.flask.secret,
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
    
    app.jinja_env.filters['is_required'] = is_required

    catalog.jinja_env.globals.update(app.jinja_env.globals)
    catalog.jinja_env.filters.update(app.jinja_env.filters)
    catalog.jinja_env.tests.update(app.jinja_env.tests)
    catalog.jinja_env.extensions.update(app.jinja_env.extensions)
    catalog.add_folder(components_dir)
    catalog.add_folder(templates_dir)

    db.init_app(app)
    migrate.init_app(app, db)
    init_database(app, db)

    login.init_app(app)

    if is_dev_environment:
        if is_docker:
            attach_debugpy(app)
        else:
            migrate_database(app, migrations_dir)

    from phasarr.blueprints.auth import auth_app
    from phasarr.blueprints.main import main_app
    from phasarr.blueprints.setup import setup_app, stages
    from phasarr.blueprints.api import api_app

    app.register_blueprint(auth_app, url_prefix="/")
    app.register_blueprint(main_app, url_prefix="/")
    app.register_blueprint(setup_app, url_prefix="/setup")
    app.register_blueprint(api_app, url_prefix="/api")

    if not app.debug and not app.testing:
        pass

    return app