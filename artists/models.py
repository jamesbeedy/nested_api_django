from __future__ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    album_musician = None
    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    def __str__(self):
        return self.name



class Song(models.Model):
    from_album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='song_album', null=True, blank=True)
    name = models.CharField(max_length=100)
    num_stars = models.IntegerField()
    def __str__(self):
        return self.name
# Create your models here.
