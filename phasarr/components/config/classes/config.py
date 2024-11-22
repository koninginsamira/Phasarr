import configparser
import os

from flask import Flask


class Config():
    app: Flask
    parser = configparser.ConfigParser()
    path: str
    default_path: str

    def __init__(self, 
                 app: Flask = None, 
                 path: str = "config.ini", default_path: str = None):
        self.path = path
        self.default_path = default_path

        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.app = app

        config_does_not_exist = not self.parser.read(self.path)

        if config_does_not_exist and self.default_path:
            default_config = configparser.ConfigParser()
            default_config.read(self.default_path)

            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            with open(self.path, "w") as config_file:
                default_config.write(config_file)
            
            self.parser.read(self.path)
    

class ConfigSection():
    config: Config
    section: str

    def __init__(self, config: Config, section: str):
        self.config = config
        self.section = section

    def __setattr__(self, key: str, value = None):
        is_not_internal = key not in ["config", "section"]

        super().__setattr__(key, value)

        if is_not_internal:
            config_path = self.config.path

            parser = self.config.parser
            parser.set(self.section, key, str(value))

            with open(config_path, "w") as config_file:
                parser.write(config_file)
                self.config.app.logger.info(
                    f'In section "{self.section}", "{key}" has been set to "{value}".')
