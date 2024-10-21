from phasarr import http_auth
from flask import Blueprint, render_template


main_app = Blueprint('main', __name__)


@main_app.route("/")
@http_auth.login_required
def index():
    return render_template("index.html")