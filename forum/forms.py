from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput, required=True)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput, required=True)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2')


class EditForm(forms.Form):
    message = forms.CharField(max_length=1000, widget=forms.Textarea)