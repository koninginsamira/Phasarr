import os
import re


def get_folders(path, limit: int = None, exclude: re.Pattern = None, __i: int = 0) -> dict:
    folders = {}
    
    if limit is None or __i < limit:
        for folder in os.listdir(path):
            if exclude and exclude.match(folder):
                continue

            full_path = os.path.join(path, folder)
            if os.path.isdir(full_path):
                folders[folder] = get_folders(
                    full_path, limit, exclude, __i = __i + 1)
            
    return folders


def remove_protocol(uri: str) -> str:
    return re.sub("^[a-zA-Z]*:/{2,3}", "", uri)