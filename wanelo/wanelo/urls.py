from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wanelo.views.home', name='home'),
    # url(r'^wanelo/', include('wanelo.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^trending$','product.toptoday'),
    url(r'^(?P<userid>[\w|\d]+)/collection/(?P<collectionid>[\w|\d]+)$','collection.collectiondetail'),
    url(r'^(?P<userid>[\w|\d]+)/collection/(?P<collectionid>[\w|\d]+)/followers$','collection.followers'),
    url(r'^top/people$','user.top'),
    url(r'^top/stores$','store.top'),
    url(r'^top/collections$','collection.top'),
    url(r'^ticker$','product.tickerview'),
    url(r'^recent$','product.recentposts'),
    url(r'^popular$','product.popular'),
    url(r'^p/post$','product.commitpost'),
    url(r'^p/(?P<productid>.+)/add_details$','product.adddetails'),
    url(r'^p/(?P<productid>.+)/submit_details$','product.submitdetails'),
    url(r'^p/(?P<productid>.+)$','product.productdetail'),
    url(r'^search?query=(?P<querystring>[\w|\d]+)$','product.search'),
    url(r'^search/people/?query=(?P<querystring>[\w|\d]+)$','users.search'),
    url(r'^store/(?P<storeid>[\w|\d]+)$','store.product'),
    url(r'^tags/(?P<tag>[\w|\d]+)/follower$','tag.followers'),
    url(r'^tags/(?P<tag>[\w|\d]+)$','tag.product'),
    url(r'^(?P<userid>[\w|\d]+)$','user.overview'),
    url(r'^(?P<userid>[\w|\d]+)/tagged$','user.taggedproduct'),
    url(r'^friends$','user.findfriends'),
    url(r'^(?P<userid>[\w|\d]+)/following$','user.feeds'),
    url(r'^(?P<userid>[\w|\d]+)/stores$','user.stores'),
    url(r'^p/(?P<productid>d+)/savers$','product.productavers'),
    url(r'^p/(?P<productid>d+)/saves$','product.saveproduct')

)
