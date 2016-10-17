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

# use ElasticSearch (v1 only)
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch',
#         'URLS': ['http://localhost:9200'],
#         'INDEX': 'wagtail',
#         'TIMEOUT': 5,
#     }
# }
