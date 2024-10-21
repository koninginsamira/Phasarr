from phasarr import app
from phasarr.blueprints.auth import auth_app
from phasarr.blueprints.main import main_app
from phasarr.blueprints.setup import setup_app
from phasarr.blueprints.api import api_app


app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(main_app, url_prefix="/")
app.register_blueprint(setup_app, url_prefix="/setup")
app.register_blueprint(api_app, url_prefix="/api")