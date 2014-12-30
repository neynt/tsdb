from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Song(models.Model):
    # A song in its original language that can be used as
    # a base for translation.
    title = models.CharField(max_length=80)
    video_url = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist)
    lyrics = models.TextField()

    def __str__(self):
        return "%s by %s" % (self.title, self.artist.name)

class SongTranslation(models.Model):
    # A translation of a song.
    orig = models.ForeignKey(Song)
    lang = models.CharField(max_length=3)
    title = models.CharField(max_length=80)
    video_url = models.CharField(max_length=80)
    translator = models.CharField(max_length=80)
    lyrics = models.TextField()

    def __str__(self):
        return "Translation of %s by %s" % (self.title, self.translator)
