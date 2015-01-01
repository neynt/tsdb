from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from tsdb.models import Artist, Song, SongTranslation
import itertools

def song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    lines = song.lyrics.split('\n')
    translations = song.songtranslation_set.all()
    context = {'song': song, 'lines': lines, 'translations': translations}
    if 'youtube' in song.video_url:
        yt_id = song.video_url.split('=')[-1]
        context['song_video'] = '<iframe width="560" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % (yt_id)
    return render(request, 'tsdb/song.html', context)

def translation(request, translation_id):
    translation = get_object_or_404(SongTranslation, pk=translation_id)
    song = translation.orig
    lines = translation.lyrics.split('\n');
    context = {'translation': translation, 'song': song, 'lines': lines}
    if 'youtube' in translation.video_url:
        yt_id = translation.video_url.split('=')[-1]
        context['song_video'] = '<iframe width="560" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % (yt_id)
    return render(request, 'tsdb/translation.html', context)

def song_and_translation(request, translation_id):
    translation = get_object_or_404(SongTranslation, pk=translation_id)
    song = translation.orig
    lines = itertools.zip_longest(song.lyrics.split('\n'), translation.lyrics.split('\n'), fillvalue="")
    context = {'translation': translation, 'song': song, 'lines': lines}
    if 'youtube' in translation.video_url:
        yt_id = translation.video_url.split('=')[-1]
        context['song_video'] = '<iframe width="560" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>' % (yt_id)
    return render(request, 'tsdb/song_and_translation.html', context)

def submit_song_action(request):
    try:
        new_song = Song()
        new_song.title = request.POST['title']
        new_song.video_url = request.POST['video_url']
        new_song.artist, created = Artist.objects.get_or_create(name=request.POST['artist'])
        new_song.lyrics = request.POST['lyrics']
        new_song.save()
        return HttpResponseRedirect(reverse('tsdb:song', args=(new_song.id,)))
    except KeyError:
        return HttpResponse("nope")

def submit_song_form(request):
    return render(request, 'tsdb/submit_song_form.html')

def submit_translation_form(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    lines = song.lyrics.split('\n')
    context = {'song': song, 'lines': lines}
    return render(request, 'tsdb/submit_translation_form.html', context)

def submit_translation_action(request, song_id):
    try:
        song = get_object_or_404(Song, pk=song_id)
        new_trans = song.songtranslation_set.create()
        new_trans.title = request.POST['title']
        new_trans.video_url = request.POST['video_url']
        new_trans.translator = request.POST['translator']
        new_trans.lyrics = request.POST['lyrics']
        new_trans.save()
        return HttpResponseRedirect(reverse('tsdb:translation', args=(new_trans.id,)))
    except KeyError:
        return HttpResponse("nope")

def submit_song_and_translation_form(request):
    return render(request, 'tsdb/submit_song_and_translation_form.html')

def index(request):
    songs = Song.objects.order_by('title')
    context = {'songs': songs}
    return render(request, 'tsdb/index.html', context)
