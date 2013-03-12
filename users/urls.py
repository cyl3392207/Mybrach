from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'register$', 'register'),
    url(r'login$', 'login'),
    url(r'logout$', 'logout'),
    url(r'profile$', 'profile'),
    url(r'forget/password$', 'forget_password'),
    url(r'reset/password$', 'reset_password'),
    url(r'check$', 'check'),
)