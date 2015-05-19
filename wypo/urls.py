
from django.conf.urls import patterns, include, url
from django.contrib import admin
from contact.views import MessageAddView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^authors/', include('shelf.urls')),
    url(r'^contact/$', MessageAddView.as_view())
    )

