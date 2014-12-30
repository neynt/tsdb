from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from tsdb.models import Song, SongTranslation

def song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    lines = song.lyrics.split('\n')
    context = {'song': song, 'lines': lines}
    return render(request, 'tsdb/song.html', context)

def translation(request, translation_id):
    translation = get_object_or_404(SongTranslation, pk=translation_id)
    song = translation.orig
    lines = translation.lyrics.split('\n');
    context = {'translation': translation, 'song': song, 'lines': lines}
    return render(request, 'tsdb/translation.html', context)

def song_and_translation(request, translation_id):
    translation = get_object_or_404(SongTranslation, pk=translation_id)
    song = translation.orig
    lines = zip(song.lyrics.split('\n'), translation.lyrics.split('\n'))
    context = {'translation': translation, 'song': song, 'lines': lines}
    return render(request, 'tsdb/song_and_translation.html', context)

def index(request):
    songs = Song.objects.order_by('title')
    context = {'songs': songs}
    return render(request, 'tsdb/index.html', context)
