###
#   CORE configuration
###

from unipath import Path

from _install.skeletton.core.utils import get_env_variable
from .variables import (
    PROJECT_PATH, _STATIC_ROOT, _MEDIA_ROOT, LOG_DIR
)


gettext = lambda s: s

STATIC_ROOT = _STATIC_ROOT
MEDIA_ROOT = _MEDIA_ROOT

TEMPLATE_DIRS = (
    PROJECT_PATH.child('templates'),
)

STATICFILES_DIRS = (
    PROJECT_PATH.child('assets'),
)

WSGI_APPLICATION = 'run.wsgi.application'
ROOT_URLCONF = '_install.skeletton.run.urls'

SITE_ID = 1

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)



# URLS:
WEBSITE_URL = get_env_variable('DJANGO_WEBSITE_URL')
STATIC_URL = get_env_variable('DJANGO_STATIC_URL')
MEDIA_URL = get_env_variable('DJANGO_MEDIA_URL')

# Security related
# ALLOWED_HOSTS = ['.<domain>'] top be set in prod
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')
DEBUG = bool(get_env_variable('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Felix Plitzko', 'felix.plitzko@libermentix.com'),
)

MANAGERS = ADMINS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
)


LANGUAGES = [
    ('NL', gettext('Nederlands')),
    ('EN', gettext('English')),
    ('DE', gettext('Deutsch')),
]


##
## South migration settings
##
SOUTH_LOGGING_ON = True
SOUTH_LOGGING_FILE = Path(LOG_DIR,'south.log')




