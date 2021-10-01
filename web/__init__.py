from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config
from config import Config
from secret_service import secrets


db = SQLAlchemy()


def init_app():
    Config.SECRET_KEY = secrets.get_flask_secret_key()
    Config.DB_PASS = secrets.get_db_instance_password()
    config.set_db_uri()

    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        # Include our Routes
        from .index import routes

        # Register Blueprints
        app.register_blueprint(index.routes.index_bp)

        return app
