import configparser

from flask import Flask


class Config():
    app: Flask
    parser = configparser.ConfigParser()
    path: str

    def __init__(self, app: Flask, path: str, default_path: str = None):
        self.app = app
        self.path = path

        config_does_not_exist = not self.parser.read(path)

        if config_does_not_exist and default_path:
            default_config = configparser.ConfigParser()
            default_config.read(default_path)

            with open(path, "w") as config_file:
                default_config.write(config_file)
            
            self.parser.read(path)
    

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
                    f'In section "{self.section}", key "{key}" has been set to "{value}".')
