from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    artist = models.CharField(max_length=50, default='Исполнитель неизвестен')
    title = models.CharField(max_length=50, default="Без названия")
    url = models.CharField(max_length=120)

    def __str__(self):
        return self.artist + " — " + self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    history_size = models.IntegerField(default=5)
    last_tracks = models.ManyToManyField(Track, blank=True)

    def __str__(self):
        return self.user.username


class HistoryEntity(models.Model):
    user_profile = models.ForeignKey(UserProfile)
    track = models.ForeignKey(Track)
    listen_date = models.DateTimeField()
