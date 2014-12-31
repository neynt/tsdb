from django.conf.urls import patterns, url
from tsdb import views

urlpatterns = patterns('',
    # e.g. /
    url(r'^$', views.index, name='index'),
    # e.g. /s/23
    url(r'^s/(?P<song_id>\d+)$', views.song, name='song'),
    # e.g. /t/69
    url(r'^t/(?P<translation_id>\d+)$', views.translation, name='translation'),
    # e.g. /ts/69
    url(r'^ts/(?P<translation_id>\d+)$', views.song_and_translation, name='song_and_translation'),
)
