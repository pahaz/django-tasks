from django.db import models

class Movie(models.Model):
    film = models.CharField(max_length=100)
    info = models.TextField(max_length=500)
    short_info = models.TextField(max_length=150)
    youtube_link = models.CharField(max_length=100)
    price = models.IntegerField()
    poster = models.ImageField(upload_to=('poster'))
    def __unicode__(self):
        return self.film