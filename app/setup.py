from flask import Blueprint


setup = Blueprint('setup', __name__)


@setup.route("/")
def index():
    return "setup"