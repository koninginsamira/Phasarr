import inspect
import re

from flask import request, current_app as app

from phasarr.api import api_app
from phasarr.components.utilities.helpers.file import get_folders


prefix = "folders"

@api_app.route(f"/{prefix}/list")
def folder_list():
    api_name = inspect.currentframe().f_code.co_name

    path = f"./{request.args.get("path", "").lstrip("/")}"
    limit = request.args.get("limit")
    limit = int(limit) if limit else None
    exclude = request.args.get("exclude")
    exclude = re.compile(exclude) if exclude else None

    app.logger.debug(f'API "{api_name}" has been called with the following arguments: {request.args.to_dict(flat=True)}')

    return get_folders(path, limit=limit, exclude=exclude)