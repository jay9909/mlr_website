from config import Config
# noinspection PyPackageRequirements
from google.cloud import secretmanager


def get_flask_secret_key():
    return get_secret(Config.FLASK_SECRET_KEY_SECRET)


def get_db_instance_password():
    return get_secret(Config.CLOUD_SQL_PASSWORD_SECRET)


def get_secret(secret_key):
    secret_client = secretmanager.SecretManagerServiceClient()
    secret_version = secret_client.access_secret_version(name=secret_key)
    return secret_version.payload.data.decode('UTF-8')
