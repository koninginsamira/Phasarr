import os


def get_dirs(path):
    dirs = {}

    for dir in os.listdir(path):
        if dir.startswith("."):
            continue

        full_path = os.path.join(path, dir)
        if os.path.isdir(full_path):
            dirs[dir] = get_dirs(full_path)
            
    return dirs