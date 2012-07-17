from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'reg.view.login'),
    url(r'^login/$', 'reg.views.do_login', name='login'),
    url(r'^logout/$', 'reg.views.do_logout', name='logout'),
    ## add your url here
)
