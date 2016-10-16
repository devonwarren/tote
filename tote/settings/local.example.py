try:
    from .production import *
except ImportError:
    pass

TWITTER_KEYS = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token_key': '',
    'access_token_secret': '',
}

# generate new secret key
SECRET_KEY = ''

# uncomment if using postgres and put in password
DATABASES['default']['password'] = ''
