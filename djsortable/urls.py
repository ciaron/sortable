#from django.conf.urls import patterns, url
from django.conf.urls import url, include
#from django.conf.urls.defaults import *

from djsortable import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # eg: /entries/5/
    url(r'^(?P<entry_id>\d+)/$', views.detail, name='detail'),
]
