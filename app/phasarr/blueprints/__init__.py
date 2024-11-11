from flask import redirect, request, url_for

from phasarr import app, config
from phasarr.blueprints.auth import auth_app
from phasarr.blueprints.main import main_app
from phasarr.blueprints.setup import setup_app, stages
from phasarr.blueprints.api import api_app
            

app.register_blueprint(auth_app, url_prefix="/")
app.register_blueprint(main_app, url_prefix="/")
app.register_blueprint(setup_app, url_prefix="/setup")
app.register_blueprint(api_app, url_prefix="/api")


@app.before_request
def before():
    current_stage = config.setup.stage
    is_blueprint = request.blueprint != None
    is_not_setup = not (request.blueprint == "setup")
    setup_is_not_done = not (current_stage > len(stages))

    if is_blueprint:
        if is_not_setup:
            if setup_is_not_done:
                return redirect(url_for("setup.setup"))