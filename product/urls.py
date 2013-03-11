from django.conf.urls import patterns, include, url


urlpatterns = patterns('product.views',
    url(r'^$', 'index'),

    url(r'^trending/', 'trending'),
    url(r'^recent/', 'recent'),
)