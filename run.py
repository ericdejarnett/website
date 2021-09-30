import flask
import json
from app.app import create_app
from app.utils.constants import CONFIG_PATH

#add command line args to pass environment in
env = "Development"
server = create_app()

with open(CONFIG_PATH, "r") as cfg_file:
    cfg = json.loads(cfg_file.read())[env]

if __name__ == '__main__':
    server.run(host = cfg["HOST"], port = cfg["PORT"])
