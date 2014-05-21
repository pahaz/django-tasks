from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField()
    author = models.ForeignKey(User)
    def __unicode__(self):
        if len(self.name) > 10:
            return self.name[0:10] + '...'
        return self.name

class Message(models.Model):
    theme = models.ForeignKey(Theme)
    text = models.CharField(max_length = 1000)
    created = models.DateTimeField()
    author = models.ForeignKey(User)
    def __unicode__(self):
        if len(self.theme.name) > 10:
            theme = self.theme.name[0:10] + '...'
        else:
            theme = self.theme.name
        if len(self.text) > 10:
            text = self.text[0:10] + '...'
        else:
            text = self.text
        return self.author.username + ' | ' + theme + ' | ' + text