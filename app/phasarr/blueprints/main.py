from flask import Blueprint

from phasarr import catalog
from phasarr.helpers.auth import login_required


main_app = Blueprint("main", __name__)


@main_app.route("/")
@login_required
def main():
    return catalog.render(
        "main.Main"
    )