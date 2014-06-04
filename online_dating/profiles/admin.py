from django.contrib import admin

# Register your models here.
from profiles.models import Profile, Vote, Comment

admin.site.register(Profile)
admin.site.register(Vote)
admin.site.register(Comment)