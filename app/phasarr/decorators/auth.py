from functools import wraps

from phasarr import http_auth, config


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_mode = config.authentication.method

        match auth_mode:
            case "prompt":
                return http_auth.login_required(func)(*args, **kwargs)
            case "form":
                pass
            case _:
                raise ValueError(
                    "Authentication mode '" + auth_mode + "' is not supported. \
                        Remove the config file to generate a correct one.")
        
    return wrapper