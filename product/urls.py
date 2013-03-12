from django.conf.urls import patterns, include, url


urlpatterns = patterns('product.views',
    url(r'^$', 'index'),

    url(r'^trending/', 'list_trending'),
    url(r'^recent/', 'list_recent'),
    url(r'^popular/', 'list_popular'),

    url(r'^search/', 'search'),

    url(r'^p/(\d+)/$', 'detail_product'),
    url(r'^p/(\d+)/(\d+)$', 'detail_save'),
)