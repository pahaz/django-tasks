from django.db import models
from django.utils.text import slugify

# Create your models here.

class Audio(models.Model):
	author = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	file = models.FileField(upload_to = 'documents/%Y/%m/%d')

	@property
	def pretty_name(self):
	    return "{0}-{1}.{2}".format(slugify(self.author), slugify(self.name), 'mp3')