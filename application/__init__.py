from flask import Flask
from flask_login import LoginManager
import os

app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"),
            static_url_path='/static',
            template_folder=os.path.join(os.getcwd(), "templates"))

login_manager = LoginManager()


def initialize():
    server_dir = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(server_dir, "..", 'config.py')
    local_config_file = os.path.join(server_dir, "..", 'local_config.py')

    app.config.from_pyfile(config_file)
    if os.path.exists(local_config_file):
        app.config.from_pyfile(local_config_file)


    from . import route
