from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('picfall.account.views',
        url(r'^login/$', 'login_view'),
        url(r'^logout/$', 'logout_view'),
)
