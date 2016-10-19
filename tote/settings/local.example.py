# 1. Copy this file to local.py
# 2. Set DJANGO_SETTINGS_MODULE to tote.settings.local
# 3. Set values below

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
# DATABASES['default']['password'] = ''

# put in mailchimp key
MAILCHIMP_API_KEY = ''

# email password for website@totemag.com
EMAIL_HOST_PASSWORD = ''
