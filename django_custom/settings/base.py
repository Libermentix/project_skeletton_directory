#################################
#   Import core settings        #
#################################
from .includes.core_settings import *
from .includes.logger import *
from .includes.async import *
from .includes.database import *
from .includes.i18n_tz import *


#################################
#    Administrator and Manager  #
#################################

ADMINS = (
    ('<Enter>', '<email>'),
)
MANAGERS = ADMINS

#################################
#   USER specific settings      #
#################################
INSTALLED_APPS += ('profiles',)
AUTH_USER_MODEL = 'profiles.AppUser'

# Authentication backend
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# deprecated
# AUTH_PROFILE_MODULE = ''
#################################
#   ADmin Shortcuts             #
#################################
# see https://github.com/alesdotio/django-admin-shortcuts/ for details
#ADMIN_SHORTCUTS = [
#
#]

################################
#   EMAIL Section              #
################################

#E-Mail Backend (get rid of mailing and put it into the console by default)
#reset this in production to django.core.mail.backends.smtp.EmailBackend
#if DEBUG:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#INSTALLED_APPS += ('djrill', )
#MANDRILL_API_KEY = get_env_variable('MANDRILL_API_KEY')
#EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
#MANDRILL_SUBACCOUNT = 'gogolf.nu'
#MANDRILL_GANALYTICS_DOMAINS = None
#MANDRILL_GANALYTICS_CAMPAIGN = None
#MANDRILL_IP_POOL = None


###########################################
# DEBUG Section for settings.Debug = TRUE #
###########################################

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) \
                     + MIDDLEWARE_CLASSES


###########################################
#   DJANGO-CMS                            #
###########################################
#MIDDLEWARE_CLASSES += (
#    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.page.CurrentPageMiddleware',
#    'cms.middleware.toolbar.ToolbarMiddleware',
#    'cms.middleware.language.LanguageCookieMiddleware',
#)
#
#TEMPLATE_CONTEXT_PROCESSORS += (
#    'cms.context_processors.media',
#    'sekizai.context_processors.sekizai',
#)
#
#INSTALLED_APPS += (
#    'djangocms_admin_style',
#    'djangocms_text_ckeditor',
#    'cms',
#    'mptt',
#    'menus',
#    'south',
#    'sekizai',
#    'djangocms_style',
#    'djangocms_column',
#    'djangocms_file',
#    'djangocms_flash',
#    'djangocms_googlemap',
#    'djangocms_inherit',
#    'djangocms_link',
#    'djangocms_picture',
#    'djangocms_teaser',
#    'djangocms_video',
#    'reversion',
#)
#
#CMS_LANGUAGES = {
    ## Customize this
#    'default': {
#        'hide_untranslated': False,
#        'redirect_on_fallback': True,
#        'public': True,
#    },
#    1: [
#        {
#            'redirect_on_fallback': True,
#            'code': 'NL',
#            'hide_untranslated': False,
#            'name': gettext('NL'),
#            'public': True,
#        },
#        {
#            'redirect_on_fallback': True,
#            'code': 'EN',
#            'hide_untranslated': False,
#            'name': gettext('EN'),
#            'public': True,
#        },
#        {
#            'redirect_on_fallback': True,
#            'code': 'DE',
#            'hide_untranslated': False,
#            'name': gettext('DE'),
#            'public': True,
#        },
#    ],
#}
#CMS_TEMPLATES = (
    ## Customize this
#    ('fullwidth.html', 'Fullwidth'),
#    ('sidebar_left.html', 'Sidebar Left'),
#    ('sidebar_right.html', 'Sidebar Right')
#)

#CMS_PERMISSION = True
#CMS_PLACEHOLDER_CONF = {}
