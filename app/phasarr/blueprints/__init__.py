from flask import redirect, request, url_for

from phasarr import app, config
from phasarr.helpers.setup import redirect_setup
from phasarr.blueprints.auth import auth_app
from phasarr.blueprints.main import main_app
from phasarr.blueprints.setup import setup_app
from phasarr.blueprints.api import api_app
            

app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(main_app, url_prefix="/")
app.register_blueprint(setup_app, url_prefix="/setup")
app.register_blueprint(api_app, url_prefix="/api")


@app.before_request
def before():
    is_blueprint = request.blueprint != None
    is_setup = request.blueprint == "setup"
    is_setup_done = config.setup.stage > 2

    if is_blueprint:
        if is_setup:
            if is_setup_done:
                return redirect(url_for("main.main"))
        else:
            if not is_setup_done:
                return redirect_setup()

    return