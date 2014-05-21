from django.contrib import admin
from forum.models import Theme, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1

class ThemeAdmin(admin.ModelAdmin):
    inlines = [MessageInline]

admin.site.register(Theme, ThemeAdmin)