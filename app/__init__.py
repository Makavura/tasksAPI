from flask import flask
from instance.config import *
from app.views.tasks_view import *

def create_app(config_by_name):
    app = Flask(__name__)
    app.register_blueprint(tasks)
    return app