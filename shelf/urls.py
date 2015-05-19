from django.conf.urls import patterns, include, url

from shelf.views import AuthorListView, AuthroDetailView

urlpatterns = patterns('',
    url(r'^autorzy/$', AuthorListView.as_view(), name='author-list'),
    url(r'^autorzy/(?P<pk>\d+)/$', AuthorDetaukView.as_view(), name='author-detail'),
    )