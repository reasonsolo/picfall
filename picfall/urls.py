from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

from picfall.api import urls as api_urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'picfall.fall.views.home', name='home'),
    url(r'^', include('picfall.fall.urls')),
    url(r'^auth/', include('picfall.account.urls')),
    url(r'api/', include(api_urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
