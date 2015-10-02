import os
import sys

SITE_ID = 1
USE_I18N = True

ADMIN_TABS =  (('Filotis', ('naturebank')),
               ('Maintenance', ('auth', 'flatpages', 'sites')),
               ('Legacy', ('naturebank_legacy')))
ADMIN_TABS_DEFAULT_NAME = 'Filotis'

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
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'filotis.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',

    # External Dependencies
    'admintabs',
    'django_filters',
    #'ajax_filtered_fields',
    'pagination',
    'django_sorting',

    #'naturebank_legacy',
    'naturebank',
)

PAGINATION_INVALID_PAGE_RAISES_404 = True

STATIC_URL = '/static/'
