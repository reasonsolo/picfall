from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('picfall.fall.views',
        url(r'^$', 'home'),
)
