from django import forms
from django.contrib import admin
from tsdb.models import Artist, Song, SongTranslation

class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'artist', 'video_url', 'lyrics']}),
    ]

admin.site.register(Artist)
admin.site.register(Song, SongAdmin)
admin.site.register(SongTranslation)
