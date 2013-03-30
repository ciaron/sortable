from django.conf.urls import patterns, url

from djsortable import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # eg: /entries/5/
    url(r'^(?P<entry_id>\d+)/$', views.detail, name='detail'),
)
