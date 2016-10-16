from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

# password is set in local 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tote',
        'USER': 'tote',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
