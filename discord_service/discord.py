import urllib

import secret_service.secrets
from config import Config
import requests

discord_api_endpoint = 'https://discord.com/api/v9'


def make_login_url(base_url):
    # Discord's authorization endpoint
    url = 'https://discord.com/api/oauth2/authorize?'

    # Fixed Params
    url += F'client_id={Config.DISCORD_APPLICATION_ID}&response_type=code&scope=identify&'

    # Redirect URL, depends on serving environment
    url += urllib.parse.quote_plus(f'redirect_uri={base_url}oauth/redirect')

    return url


def get_access_token(code, base_url):
    data = {
        'client_id': Config.DISCORD_APPLICATION_ID,
        'client_secret': secret_service.secrets.get_discord_client_secret(),
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'https://redditball-test-yxax2m5aqa-uk.a.run.app/'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    r = requests.post(f'{discord_api_endpoint}/oauth2/token', data=data, headers=headers)
    r.raise_for_status()

    return r.json()
