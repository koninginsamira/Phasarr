from functools import wraps

import flask_login

from flask_login import current_user
from phasarr import http_auth, config


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_mode = config.authentication.method

        if not current_user.is_authenticated:
            match auth_mode:
                case "prompt":
                    return http_auth.login_required(func)(*args, **kwargs)
                case "form":
                    return flask_login.login_required(func)(*args, **kwargs)
                case _:
                    raise ValueError(
                        "Authentication mode '" + auth_mode + "' is not supported. \
                            Remove the config file to generate a correct one.")
        else:
            return func(*args, **kwargs)
        
    return wrapper