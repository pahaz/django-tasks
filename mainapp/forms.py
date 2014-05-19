from django import forms
from mainapp.models import UserProfile
from django.contrib.auth.models import User


class DocumentForm(forms.Form):
    price = forms.FloatField(min_value=0.0)
    docfile = forms.FileField(
        label='Upload files here!',
    )


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
