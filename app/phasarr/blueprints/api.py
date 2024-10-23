import time

from flask import Blueprint


api_app = Blueprint("api", __name__)


@api_app.route("/time")
def get_current_time():
    return {"time": time.time()}