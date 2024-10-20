import time

from flask import Blueprint


api = Blueprint('api', __name__)


@api.route("/time")
def get_current_time():
    return {"time": time.time()}