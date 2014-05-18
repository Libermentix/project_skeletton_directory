from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

#uncomment for use with django cms
#from cms.sitemaps import CMSSitemap
#urlpatterns += i18n_patterns('',
#                            url(
#                                r'^sitemap\.xml$',
#                                'django.contrib.sitemaps.views.sitemap',
#                                {'sitemaps': {'cmspages': CMSSitemap}}),
#                            url(r'^', include('cms.urls')),
#)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + staticfiles_urlpatterns() + urlpatterns
