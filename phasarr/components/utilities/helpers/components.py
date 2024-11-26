import importlib
import os
from pathlib import Path
from flask import Flask
from jinjax import Catalog


def import_components(app: Flask, catalog: Catalog, components_folder: str):
    components = {f.name:f.path for f in os.scandir(components_folder) if f.is_dir()}
    for component, path in components.items():
        for root, folders, files in os.walk(path):
            for folder in folders:
                if folder == "templates":
                    templates_path = os.path.join(root, folder)
                    fragments_file = Path(os.path.join(templates_path, "fragments.py"))

                    catalog.add_folder(templates_path, prefix=component)

                    if fragments_file.is_file():
                        fragments = import_from_path("fragments", fragments_file)

                        app.register_blueprint(fragments)


def import_from_path(module: str, path: str):
    spec = importlib.util.spec_from_file_location(module, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module