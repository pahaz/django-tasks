from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class PeopleManager(models.Manager):
	def get_queryset(self):
		return super(PeopleManager, self).get_queryset()


class RandomProfilesManager(models.Manager):
	def get_queryset(self):
		return super(RandomProfilesManager, self).get_queryset().order_by('?')[:5]


class Profile(models.Model):
	GENDER_CHOICE = (
		("m", "male"),
		("f", "female"),
		("other", "???")
	)

	owner = models.OneToOneField(User, primary_key=True)
	photo = models.ImageField(upload_to="photo", null=True, blank=True)
	birthday = models.DateField(null=True,)
	name = models.CharField(max_length=30)
	gender = models.CharField(choices=GENDER_CHOICE, max_length=5, default="other")
	about = models.CharField(max_length=200, blank=True)

	objects = PeopleManager()
	random_profiles = RandomProfilesManager()

	def __unicode__(self):
		return self.name

	def average_rate(self):
		avg = self.vote_set.aggregate(Avg('score')).get('score__avg')
		if avg:
			return round(avg, 1)
		else:
			return 0


class Comment(models.Model):
	profile = models.ForeignKey(Profile)
	user = models.ForeignKey(User)
	text = models.CharField(max_length=200)

	def __unicode__(self):
		return self.user.__repr__() + ": " + self.text


class Vote(models.Model):
	VOTE_CHOICE = (
		(1,"awful"),
		(2,"bad"),
		(3,"ok"),
		(4,"good"),
		(5,"awesome")
	)
	score = models.IntegerField(choices=VOTE_CHOICE)
	for_whom = models.ForeignKey(Profile)
	from_whom = models.ForeignKey(User)

	def __unicode__(self):
		return self.for_whom.name + " is " + str(self.score)
