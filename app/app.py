from flask import Flask, Blueprint, render_template, abort
import json
from app.utils.constants import CONFIG_PATH
from app.controllers.homepage import homepage

def create_app(env = "Development"):
    app = Flask(__name__)
    #load config values
    cfg_dict = None
    try:
        with open(CONFIG_PATH, "r") as cfg_file:
            cfg_dict = json.loads(cfg_file.read())
            print(cfg_dict)
        app.config.from_mapping(cfg_dict[str(env)])
    except FileNotFoundError as ex:
        print("Config error - file was not found; check that the config file is available")
    except KeyError as ex:
        print("Config error - the specified environment "+env+" isn't available in the config")
        raise
    #register blueprints
    app.register_blueprint(homepage)
    
    return app
