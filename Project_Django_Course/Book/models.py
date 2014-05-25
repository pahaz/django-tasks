from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pay(models.Model):
    class Meta():
        db_table = "Pays"
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Author(models.Model):
    class Meta():
        db_table = "Authors"

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    photo = models.ImageField(upload_to='/media/Photo_Books/', blank=True)


    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    class Meta():
        db_table = "Books"

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publication_date = models.DateField()
    likes = models.IntegerField(default=0)
    price = models.IntegerField(default=500)
    photo = models.ImageField(upload_to='Photo_Books', blank=True)
    #owns_names = models.CharField(max_length=1000, blank=True, default=0)
    owns_names = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    class Meta():
        db_table = "Comments"

    comments_text = models.TextField(verbose_name='Текст комментария', default=' ')
    comments_books = models.ForeignKey(Book)

#class MyType(User):
#    class Meta():
#        db_table = "Users"
#
#    list_of_books = models.ManyToManyField(Book)
