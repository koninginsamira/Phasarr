import os
from jinjax import Catalog


def import_templates_from_components(catalog: Catalog, components_folder: str):
    components = {f.name:f.path for f in os.scandir(components_folder) if f.is_dir()}
    for component, path in components.items():
        for root, folders, files in os.walk(path):
            for folder in folders:
                if folder == "templates":
                    templates_path = os.path.join(root, folder)
                    catalog.add_folder(templates_path, prefix=component)