import os
import requests

from flask import Blueprint, Flask, request, url_for
from jinjax import Catalog


current_folder = os.path.dirname(__file__)
component_name = "tree"


def import_component(app: Flask, catalog: Catalog):
    import_fragments(app, catalog)
    import_templates(catalog)


def import_templates(catalog: Catalog):
    templates_folder = os.path.join(current_folder, "templates")

    catalog.add_folder(templates_folder, prefix=component_name)


def import_fragments(app: Flask, catalog: Catalog):
    fragments = Blueprint(component_name, __name__,
                          template_folder=current_folder)
    

    @fragments.route("/view")
    def view():
        args = request.args

        tree = request.json
        
        return catalog.render(
            f"{component_name}.view.TreeView",
            tree=tree,
            **args
        )
    
    
    @fragments.route("/view_from_api")
    def view_from_api():
        api = request.args.get("api")
        args = request.args.to_dict(flat=True)

        try:
            response = requests.get(api, params=args)
        except requests.exceptions.MissingSchema:
            local_api = f"{request.host_url.rstrip('/')}{api}"

            app.logger.debug(f'API "{api}" is missing a scheme (probably because it is an API on the same domain), so it has been converted to: "{local_api}"')
            response = requests.get(local_api, params=args)

        if response.status_code != 200:
            error = f'API "{api}" returned status code {response.status_code}, with the following message: "{response.text}"'

            app.logger.error(error)
            return error, 500

        if response.status_code == 200:
            tree = response.json()

            if tree:
                return catalog.render(
                    f"{component_name}.view.TreeViewFromAPI",
                    tree=tree,
                    **args
                )
            else:
                return "", 204
    

    app.register_blueprint(fragments, url_prefix=f"/fragments/{component_name}")