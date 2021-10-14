import os
import sys

SITE_ID = 1
USE_I18N = True

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django_sorting.middleware.SortingMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'naturebank_project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    # External Dependencies
    'django_filters',
    'pagination',
    'django_sorting',
    'naturebank',
)

##TEMPLATE_DIRS = ('/home/naturebank/nb/naturebank-filotis/templates/',)
##STATICFILES_DIRS = ('/home/naturebank/nb/naturebank-filotis/static/',)

PAGINATION_INVALID_PAGE_RAISES_404 = True

STATIC_URL = '/static/'

FIXTURE_DIRS = (
   '/fixtures/',
)
