import os

# Ports
debug_port = int(os.environ.get("DEBUG_PORT", "5678"))

# Paths
config_folder = os.environ.get("CONFIGPATH")
config_file = os.path.join(config_folder, "config.ini")
db_file = os.path.join(config_folder, "database.db")

app_folder = os.path.dirname(os.path.realpath(__file__))
components_folder = os.path.join(app_folder, "components")
templates_folder = os.path.join(app_folder, "templates")

defaults_folder = os.path.join(app_folder, "defaults")
default_config_file = os.path.join(defaults_folder, "config.ini")

# Checks
is_docker = int(os.environ.get("DOCKER", "0"))