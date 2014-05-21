from django.contrib import admin
from music.models import Track, UserProfile


class TrackAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'url')

admin.site.register(Track, TrackAdmin)
admin.site.register(UserProfile)

