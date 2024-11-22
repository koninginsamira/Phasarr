import os
from flask import Blueprint


base_folder = os.path.dirname(os.path.realpath(__file__))
templates_folder = os.path.join(base_folder, "templates")

auth_app = Blueprint("auth", __name__, template_folder=templates_folder)


from phasarr.auth import helper, login