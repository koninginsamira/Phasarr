import os
from flask import Blueprint


stages = {
    "authentication": {
        "name": "Authentication",
        "icon": "fa-key",
        "skippable": 0,
        "url": "setup.authentication"
    },
    "libraries": {
        "name": "Libraries",
        "icon": "fa-folder-tree",
        "skippable": 0,
        "url": "setup.libraries"
    },
    "download": {
        "name": "Download",
        "icon": "fa-cloud-arrow-down",
        "skippable": 0,
        "url": "setup.download"
    }
}

base_folder = os.path.dirname(os.path.realpath(__file__))
templates_folder = os.path.join(base_folder, "templates")

setup_app = Blueprint("setup", __name__, template_folder=templates_folder)


from phasarr.setup import helper, index, authentication, libraries, download