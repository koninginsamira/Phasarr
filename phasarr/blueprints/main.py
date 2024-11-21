from flask import Blueprint

from phasarr import catalog
from phasarr.decorators.auth import login_required


main_app = Blueprint("main", __name__)


@main_app.before_request
@login_required
def before():
    pass


@main_app.route("/")
def main():
    return catalog.render(
        "main.Main"
    )