import os
import re


def get_folders(path) -> dict:
    folders = {}

    for folder in os.listdir(path):
        if folder.startswith("."):
            continue

        full_path = os.path.join(path, folder)
        if os.path.isdir(full_path):
            folders[folder] = get_folders(full_path)
            
    return folders


def remove_protocol(uri: str) -> str:
    return re.sub("^[a-zA-Z]*:/{2,3}", "", uri)