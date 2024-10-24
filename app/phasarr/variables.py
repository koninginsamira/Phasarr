import os


base_dir = os.path.abspath(os.path.dirname(__file__))

defaults_dir = os.path.join(base_dir, "defaults")
default_config_path = os.path.join(defaults_dir, "config.ini")

components_dir = os.path.join(base_dir, "components")
templates_dir = os.path.join(base_dir, "templates")

config_dir = os.path.join(base_dir, os.environ.get("CONFIGPATH", "config"))
db_path = os.path.join(config_dir, "database.db")
config_path = os.path.join(config_dir, "config.ini")


is_dev_environment = os.environ.get("FLASK_ENV", "development") == "development"
is_docker = int(os.environ.get("DOCKER", "0"))
is_local = __name__ == "__main__"