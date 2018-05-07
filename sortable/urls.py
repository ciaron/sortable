from django.conf.urls import url, include

from djsortable import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
#    url(r'^entries/', include('djsortable.urls')),
#    url(r'^admin/', include(admin.site.urls)),
#)
urlpatterns = [
    url(r'^entries/', include('djsortable.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
