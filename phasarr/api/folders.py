import re
from flask import request

from phasarr.api import api_app
from phasarr.components.utilities.helpers.file import get_folders


prefix = "folders"

@api_app.route(f"/{prefix}/list")
@api_app.route(f"/{prefix}/list/<path:path>")
def list(path: str = ""):
    path = "./" + path
    limit = request.args.get("limit")
    limit = int(limit) if limit else None
    offset = request.args.get("offset")
    offset = int(offset) if offset else None
    exclude = request.args.get("exclude")
    exclude = re.compile(exclude) if exclude else None

    return get_folders(path, limit=limit, offset=offset, exclude=exclude)