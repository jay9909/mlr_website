import urllib

from secret_service import secrets
from config import Config
import requests
from datetime import datetime, timedelta

discord_api_endpoint = 'https://discord.com/api/v9'
discord_auth_url = 'https://discord.com/api/oauth2/authorize'
discord_token_url = 'https://discord.com/api/oauth2/token'


def make_login_url(base_url):
    redirect_url = base_url + 'oauth/redirect'
    redirect_url = urllib.parse.quote_plus(redirect_url)

    return (f'{discord_auth_url}?response_type=code&scope=identify&'
            f'client_id={secrets.get_discord_client_id()}&'
            f'redirect_uri={redirect_url}')


def get_access_token(code, base_url):
    data = {
        'client_id': secrets.get_discord_client_id(),
        'client_secret': secrets.get_discord_client_secret(),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': base_url
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(discord_token_url, data=data, headers=headers)
    r.raise_for_status()

    return create_session(r.json())


def create_session(auth_response):
    # Of the form:
    # {
    #     "access_token": "EU8T2KGsDfVfLvC8MIQTsRAZeg3Wy5",
    #     "expires_in": 604800,
    #     "refresh_token": "MV5QITeT2z6V25rLbo2ZeJKrVdpRK3",
    #     "scope": "identify",
    #     "token_type": "Bearer"
    # }

    valid_for = timedelta(seconds=float(auth_response['expires_in']))
    expiration = datetime.utcnow() + valid_for

    access_token = auth_response['access_token']
    request_headers = {
        'Authorization': f'Bearer {access_token}'
    }

    r = requests.get(f'{discord_api_endpoint}/users/@me', headers=request_headers)
    r.raise_for_status()

    # {
    #     "accent_color": null,
    #     "avatar": "fb8ce6f7a02416fadf741fa9598b1f3d",
    #     "banner": null,
    #     "banner_color": null,
    #     "discriminator": "3900",
    #     "flags": 0,
    #     "id": "340259904063406080",
    #     "locale": "en-US",
    #     "mfa_enabled": true,
    #     "premium_type": 2,
    #     "public_flags": 0,
    #     "username": "jay9909"
    # }

    return r.json()
