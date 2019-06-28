from flask import Flask
from instance.config import *
from app.views.tasks_view import tasks

def create_app(config_by_name):
    app = Flask(__name__)
    app.register_blueprint(tasks)
    return app