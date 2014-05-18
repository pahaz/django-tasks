from django.db import models
import os
# Create your models here.
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

class MovieField(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField()
    poster = models.ImageField(
        upload_to=os.path.join(PROJECT_PATH, "media")
    )

    def __unicode__(self):
        return self.name
