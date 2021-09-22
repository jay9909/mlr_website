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
    DB_SOCKET_DIR = environ.get('DB_SOCKET_DIR')
    CLOUD_SQL_CONNECTION_NAME = environ.get('CLOUD_SQL_CONNECTION_NAME')
    DB_USER = environ.get('DB_USER')
    DB_NAME = environ.get('DB_NAME')
    DB_PASS = ''  # Populated via SecretManager during app startup
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql:///{DB_NAME}?unix_socket={DB_SOCKET_DIR}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Call after setting DB_PASS after secret fetch


def set_db_uri():
    Config.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://devserver@/{Config.DB_NAME}?unix_socket={Config.DB_SOCKET_DIR}&password={Config.DB_PASS}'

