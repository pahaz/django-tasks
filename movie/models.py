from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Movie(models.Model):
    film = models.CharField(max_length=100)
    info = models.TextField(max_length=500)
    short_info = models.TextField(max_length=150)
    youtube_link = models.CharField(max_length=100)
    price = models.IntegerField()
    poster = models.ImageField(upload_to=('poster'))
    def __unicode__(self):
        return self.film

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, default='')
    status = models.CharField(null=True, blank=True, max_length=50)
    avatar = models.ImageField(upload_to="avatars",
                               default="avatars/noavatar.png",
                               null=True, blank=True)
    balance = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    filmset = models.ManyToManyField(Movie)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Pay(models.Model):
    class Meta():
        db_table = "Pays"
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name