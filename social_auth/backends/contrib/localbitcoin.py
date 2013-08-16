"""
settings.py should include the following:

    LOCALBITCOIN_CLIENT_ID = '...'
    LOCALBITCOIN_CLIENT_SECRET = '...'

Optional scope to include 'email' and/or 'messages' separated by space:

    LOCALBITCOIN_AUTH_EXTRA_ARGUMENTS = {'scope': 'email messages'}

More information on scope can be found at https://localbitcoins.com/api-docs/
"""
from urllib import urlencode

from django.utils import simplejson

from social_auth.backends import BaseOAuth2, OAuthBackend
from social_auth.utils import dsa_urlopen


LOCALBITCOIN_SERVER = 'localbitcoins.com'
LOCALBITCOIN_AUTHORIZATION_URL = 'https://localbitcoins.com/oauth2/authorize/'
LOCALBITCOIN_ACCESS_TOKEN_URL = 'https://localbitcoins.com/oauth2/access_token/'
LOCALBITCOIN_CHECK_AUTH = 'https://localbitcoin.com/api/myself'


class LocalBitcoinBackend(OAuthBackend):
    name = 'localbitcoin'

    def get_user_id(self, details, response):
        return response['id']

    def get_user_details(self, response):
        fields = ["username","trading_partners_count","feedbacks_unconfirmed_count",
                  "trading_volume_text","has_common_trades","confirmed_trade_count_text",
                  "blocked_count","feedback_count","url","trusted_count"]
        return dict([(field,response['data'][field]) for field in fields])

class LocalBitcoinAuth(BaseOAuth2):
    """LocalBitcoin OAuth mechanism"""
    AUTHORIZATION_URL = LOCALBITCOIN_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = LOCALBITCOIN_ACCESS_TOKEN_URL
    AUTH_BACKEND = LocalBitcoinBackend
    SETTINGS_KEY_NAME = 'LOCALBITCOIN_CLIENT_ID'
    SETTINGS_SECRET_NAME = 'LOCALBITCOIN_CLIENT_SECRET'
    REDIRECT_STATE = False
    STATE_PARAMETER = False

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        params = {'access_token': access_token}
        url = LOCALBITCOIN_CHECK_AUTH + '?' + urlencode(params)
        try:
            return simplejson.load(dsa_urlopen(url))
        except ValueError:
            return None


# Backend definition
BACKENDS = {
    'localbitcoin': LocalBitcoinAuth,
}
