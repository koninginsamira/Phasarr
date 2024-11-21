import os

# Ports
debug_port = int(os.environ.get("DEBUG_PORT", "5678"))

# Paths
migrations_dir = "migrations"

config_dir = os.environ.get("CONFIGPATH")
config_path = os.path.join(config_dir, "config.ini")
db_path = os.path.join(config_dir, "database.db")

app_dir = os.path.dirname(os.path.realpath(__file__))
components_dir = os.path.join(app_dir, "components")
templates_dir = os.path.join(app_dir, "templates")

defaults_dir = os.path.join(app_dir, "defaults")
default_config_path = os.path.join(defaults_dir, "config.ini")

# Checks
is_docker = int(os.environ.get("DOCKER", "0"))
is_local = __name__ == "__main__"