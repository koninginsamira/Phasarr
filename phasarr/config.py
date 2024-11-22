import secrets
from flask import Flask
from phasarr.components.config.classes.config import Config, ConfigSection


class Setup(ConfigSection):
    stage: int

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        parser = self.config.parser[self.section]
        self.stage = int(parser.get("stage") or "0")


class Flask(ConfigSection):
    secret: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        parser = self.config.parser[self.section]
        self.secret = parser.get("secret") or secrets.token_hex()


class Authentication(ConfigSection):
    method: str

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        parser = self.config.parser[self.section]
        self.method = parser.get("method")


class PhasarrConfig(Config):
    flask: Flask
    authentication: Authentication
    setup: Setup

    def init_app(self, *args, **kwargs):
        super().init_app(*args, **kwargs)

        self.flask = Flask(self, "Flask")
        self.authentication = Authentication(self, "Authentication")
        self.setup = Setup(self, "Setup")