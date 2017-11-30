from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hsk/(?P<level>[1-6]{1})/$', views.hsk, name='HSK'),
    url(r'^(?P<word_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^total/$', views.total, name='total')
]
