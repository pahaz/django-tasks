from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser


class ChatUserManager(BaseUserManager):
    def create_user(self, username, date_of_birth, password=None):

        user = self.model(
            username=self.username,
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class ChatUser(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, default='')
    status = models.CharField(null=True, blank=True, max_length=50)
    avatar = models.ImageField(upload_to="static/avatars",
                               default="static/avatars/noavatar.png",
                               null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = ChatUserManager()

    USERNAME_FIELD = 'username'
    #REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserFriends(models.Model):
    friend_list = models.ManyToManyField(ChatUser)


class Message(models.Model):
    message = models.CharField(max_length=500, null=True, blank=True)
    from_user = models.ForeignKey(ChatUser, unique=False, related_name="from", null=True)
    to_user = models.ForeignKey(ChatUser,  unique=False, related_name="to", null=True)
    is_read = models.BooleanField(default=False, unique=False)
    datetime = models.DateTimeField(null=True, blank=True)


