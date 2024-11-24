import os
import re


def get_folders(path, limit: int = None, offset: int = None, exclude: re.Pattern = None) -> dict:
    offset = offset or 0
    folders = {}
    
    if limit is None or offset < limit:
        for folder in os.listdir(path):
            if exclude and exclude.match(folder):
                continue

            full_path = os.path.join(path, folder)
            if os.path.isdir(full_path):
                folders[folder] = get_folders(
                    full_path, limit, offset + 1, exclude)
            
    return folders


def remove_protocol(uri: str) -> str:
    return re.sub("^[a-zA-Z]*:/{2,3}", "", uri)