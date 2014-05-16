from django.db import models
from django.contrib.auth.models import User
import os.path


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def filename(self):
        return os.path.basename(self.docfile.name)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    credits = models.DecimalField(default=100, max_digits=5, decimal_places=1)
    purchased_documents = models.ManyToManyField(Document)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username