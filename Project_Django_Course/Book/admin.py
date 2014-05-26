from django.contrib import admin
from Book.models import Comments, Book, Author, Pay
# Register your models here.

class BooksInline(admin.StackedInline):
    model = Comments
    extra = 2

class BookAdmin(admin.ModelAdmin):
    inlines = [BooksInline]
    list_filter = ['publication_date']

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Pay)