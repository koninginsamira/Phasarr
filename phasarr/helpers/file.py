import os
import re


def get_dirs(path) -> dict:
    dirs = {}

    for dir in os.listdir(path):
        if dir.startswith("."):
            continue

        full_path = os.path.join(path, dir)
        if os.path.isdir(full_path):
            dirs[dir] = get_dirs(full_path)
            
    return dirs


def remove_protocol(uri: str) -> str:
    return re.sub("^[a-zA-Z]*:/{2,3}", "", uri)