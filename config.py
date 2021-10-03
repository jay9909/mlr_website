"""Flask configuration variables."""
import urllib.parse
from os import environ
import os

from configparser import ConfigParser

settings = ConfigParser()
settings.read('secrets.ini')


class Config:
    # Flask Config Variables
    HOST = environ.get('HOST', '0.0.0.0')
    PORT = environ.get('PORT', '8080')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    SECRET_KEY = settings['FLASK']['SECRET_KEY']
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    if FLASK_ENV == 'development':
        SESSION_COOKIE_SECURE = False
    else:
        SESSION_COOKIE_SECURE = True

    # Database
    DB_HOST = settings['DATABASE']['HOST']
    DB_PORT = settings['DATABASE']['PORT']
    DB_USER = settings['DATABASE']['USER']
    DB_NAME = settings['DATABASE']['NAME']
    DB_PASS = settings['DATABASE']['PASS']
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Discord App Parameters
    DISCORD_APP_NAME = settings['DISCORD']['APP_NAME']
    DISCORD_CLIENT_ID = settings['DISCORD']['CLIENT_ID']
    DISCORD_APP_PUBLIC_KEY = settings['DISCORD']['PUBLIC_KEY']
    DISCORD_CLIENT_SECRET = settings['DISCORD']['CLIENT_SECRET']


def make_discord_login_url(base_url):
    encoded_base_url = urllib.parse.quote_plus(base_url)

    return (f'https://discord.com/api/oauth2/authorize?response_type=code&scope=identify&'
            f'client_id={Config.DISCORD_CLIENT_ID}&'
            f'redirect_url={encoded_base_url}/redirect'
            )
