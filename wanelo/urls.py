from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wanelo.views.home', name='home'),
    # url(r'^wanelo/', include('wanelo.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^trending/', 'product.views.trending'),
    url(r'^recent/', 'product.views.recent'),
)
