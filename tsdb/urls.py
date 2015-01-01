from django.conf.urls import patterns, url
from tsdb import views

urlpatterns = patterns('',
    # e.g. /
    url(r'^$', views.index, name='index'),
    # e.g. /song/23
    url(r'^song/(?P<song_id>\d+)$', views.song, name='song'),
    # e.g. /t/69
    url(r'^t/(?P<translation_id>\d+)$', views.translation, name='translation'),
    # e.g. /both/69
    url(r'^both/(?P<translation_id>\d+)$', views.song_and_translation, name='song_and_translation'),
    # i.e. /submit-song
    url(r'^submit-song$', views.submit_song_form, name='submit_song_form'),
    # i.e. /submit-song-action
    url(r'^submit-song-action$', views.submit_song_action, name='submit_song_action'),
    # i.e. /submit-both
    url(r'^submit-both$', views.submit_song_and_translation_form, name='submit_song_and_translation_form'),
    # e.g. /song/23/submit-translation
    url(r'^song/(?P<song_id>\d+)/submit-translation$', views.submit_translation_form, name='submit_translation_form'),
    # e.g. /song/23/submit-translation-action
    url(r'^song/(?P<song_id>\d+)/submit-translation-action$', views.submit_translation_action, name='submit_translation_action'),
)
