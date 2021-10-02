import flask
import json
import os.path

from app.app import create_app
from app.utils.constants import CONFIG_PATH
from app.utils.db_utils import init_db

#add command line args to pass environment in
env = "Development"
server = create_app()
if not os.path.exists("database.db"):
    init_db()

with open(CONFIG_PATH, "r") as cfg_file:
    cfg = json.loads(cfg_file.read())[env]

if __name__ == '__main__':
    server.run(host = cfg["HOST"], port = cfg["PORT"])
