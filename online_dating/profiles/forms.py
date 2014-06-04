from django import forms
from models import Comment, Profile, Vote

class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		exclude = ('user', 'profile')

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		exclude = ('owner',)

class VoteForm(forms.ModelForm):

	class Meta:
		model = Vote
		exclude = ('for_whom','from_whom')