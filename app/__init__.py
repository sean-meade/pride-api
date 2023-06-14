from flask import Flask 

from .extensions import api, db
from .resources import ns

import os

def create_app():
    app = Flask(__name__)

    if os.environ.get('DEVELOPMENT'):
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    else:
        os.environ.get('DATABASE_URL')

    api.init_app(app)
    db.init_app(app)

    # Adds routes to swagger
    api.add_namespace(ns)

    return app