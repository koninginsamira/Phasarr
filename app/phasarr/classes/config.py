import configparser
import secrets

from phasarr.variables import config_path, default_config_path


class _FlaskConfig():
    __config: configparser.ConfigParser
    secret: str

    def __init__(self, config: configparser.ConfigParser):
        self.__dict__["_FlaskConfig__config"] = config
        self.__dict__["secret"] = self.__config.get("Flask", "secret")

    def __setattr__(self, key: str, value: None):
        super().__setattr__(key, value)
        self.__config.set("Flask", key, value)

        with open(config_path, "w") as config_file:
            self.__config.write(config_file)


class _AuthenticationConfig():
    __config: configparser.ConfigParser
    method: str

    def __init__(self, config: configparser.ConfigParser):
        self.__dict__["_AuthenticationConfig__config"] = config
        self.__dict__["method"] = self.__config.get("Authentication", "method")

    def __setattr__(self, key: str, value: None):
        super().__setattr__(key, value)
        self.__config.set("Authentication", key, value)

        with open(config_path, "w") as config_file:
            self.__config.write(config_file)


class Config:
    __config = configparser.ConfigParser()
    flask: _FlaskConfig
    authentication: _AuthenticationConfig

    def __init__(self):     
        config_exists = self.__config.read(config_path)

        if not config_exists:
            default_config = configparser.ConfigParser()
            default_config.read(default_config_path)
            default_config.set("Flask", "secret", secrets.token_hex())

            with open(config_path, "w") as config_file:
                default_config.write(config_file)
            
            self.__config.read(config_path)

        self.__dict__["flask"] = _FlaskConfig(self.__config)
        self.__dict__["authentication"] = _AuthenticationConfig(self.__config)

    def __setattr__(self):
        raise AttributeError("Config section cannot be set directly, only change underlying options.")