from flask import Flask, Blueprint, render_template, abort
import json
from app.utils.constants import CONFIG_PATH
from app.controllers.homepage import homepage
from app.controllers.about import about
from app.controllers.contact import contact

def create_app(env = "Development"):
    app = Flask(__name__)
    #load config values
    cfg_dict = None
    try:
        with open(CONFIG_PATH, "r") as cfg_file:
            cfg_dict = json.loads(cfg_file.read())
        app.config.from_mapping(cfg_dict[str(env)])
    except FileNotFoundError as ex:
        print("Config error - file was not found; check that the config file is available")
        #TODO: add logging here
    except KeyError as ex:
        print("Config error - the specified environment "+env+" isn't available in the config")
        #TODO: add logging here
        raise
    #register blueprints
    app.register_blueprint(homepage)
    app.register_blueprint(about)
    app.register_blueprint(contact)
    
    return app
