import os
from flask import Blueprint

base_folder = os.path.dirname(os.path.realpath(__file__))
templates_folder = os.path.join(base_folder, "templates")

main_app = Blueprint("main", __name__, template_folder=templates_folder)


from phasarr.main import index