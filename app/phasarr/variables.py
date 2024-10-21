import os


base_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(base_dir, os.environ.get("CONFIGPATH", "config"))
db_path = os.path.join(config_path, "database.db")

is_dev_environment = os.environ.get("FLASK_ENV", "development") == "development"
is_docker = int(os.environ.get("DOCKER", "0"))
is_local = __name__ == "__main__"