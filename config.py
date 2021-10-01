"""Flask configuration variables."""
import urllib.parse
from os import environ


class Config:
    """Set Flask configuration from .env file."""

    # Flask Config Variables
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    SECRET_KEY = ''  # Populated via SecretManager during app startup
    HOST = environ.get('HOST', '0.0.0.0')
    PORT = environ.get('PORT', '8080')
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    if FLASK_ENV == 'development':
        SESSION_COOKIE_SECURE = False
    else:
        SESSION_COOKIE_SECURE = True

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

    # Discord App Parameters
    DISCORD_APP_NAME = environ.get('DISCORD_APP_NAME')
    DISCORD_CLIENT_ID_SECRET = environ.get('DISCORD_CLIENT_ID_SECRET')
    DISCORD_APP_PUBLIC_KEY = environ.get('DISCORD_APP_PUBLIC_KEY')
    # GCP Secret Manager resource for the Discord client secret
    DISCORD_CLIENT_SECRET_SECRET = environ.get('DISCORD_CLIENT_SECRET_SECRET')


def set_db_uri():
    Config.SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://devserver@/{Config.DB_NAME}?unix_socket={Config.DB_SOCKET_DIR}&password={Config.DB_PASS}'


def make_discord_auth_url(base_url):
    # Protocol, Host, and Path
    url = 'https://discord.com/api/oauth2/authorize?'

    # Fixed Params
    url += 'client_id=892172573507477555&response_type=code&scope=identify&'

    # Redirect URL, depends on serving environment
    url += urllib.parse.quote_plus(f'redirect_uri={base_url}oauth/redirect')

    return url
