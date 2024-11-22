import time

from phasarr.api import api_app


@api_app.route("/time")
def get_current_time():
    return {"time": time.time()}