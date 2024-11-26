import os

from flask import Blueprint, Flask
from jinjax import Catalog


current_folder = os.path.dirname(__file__)
component_name = "form"


def import_component(app: Flask, catalog: Catalog):
    import_fragments(app, catalog)
    import_templates(catalog)


def import_templates(catalog: Catalog):
    templates_folder = os.path.join(current_folder, "templates")

    catalog.add_folder(templates_folder, prefix=component_name)


def import_fragments(app: Flask, catalog: Catalog):
    fragments = Blueprint(component_name, __name__,
                          template_folder=current_folder)
    

    @fragments.route("/")
    def test():
        return "Test", 200

    app.register_blueprint(fragments, url_prefix=f"/fragments/{component_name}")