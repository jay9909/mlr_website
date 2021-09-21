"""Flask configuration variables."""
from os import environ


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    FLASK_SECRET_KEY = ''  # Populated via SecretManager during app startup
    HOST = environ.get('HOST', '0.0.0.0')
    PORT = environ.get('PORT', '8080')

    # Google Cloud Config
    FLASK_SECRET_KEY_SECRET = environ.get('FLASK_SECRET_KEY_SECRET')
    CLOUD_SQL_PASSWORD_SECRET = environ.get('DB_PWD_SECRET')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_SOCKET_DIR = environ.get('DB_SOCKET_DIR')
    CLOUD_SQL_CONNECTION_NAME = environ.get('CLOUD_SQL_CONNECTION_NAME')
    DB_USER = environ.get('DB_USER')
    DB_NAME = environ.get('DB_NAME')
    DB_PASS = ''  # Populated via SecretManager during app startup
