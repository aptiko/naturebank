from naturebank_el.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SECRET_KEY = 'dummy'
MEDIA_URL = '/site_media/'
MEDIA_ROOT = 'site_media'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'naturebank_el',
        'USER': 'naturebank_admin',
        'PASSWORD': 'topsecret',
        'HOST': 'localhost',
    }
}
