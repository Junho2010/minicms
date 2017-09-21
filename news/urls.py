from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^column/(?P<pk>\d+)/(?P<column_slug>[^/]+)/$', column_detail, name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', article_detail, name='article'),
]