import time

from flask import Blueprint

from phasarr.decorators.auth import login_required


api_app = Blueprint("api", __name__)


@api_app.before_request
@login_required
def before():
    pass


@api_app.route("/time")
def get_current_time():
    return {"time": time.time()}