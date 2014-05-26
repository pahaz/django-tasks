from django.contrib.auth.forms import UserCreationForm
from django.db import models

class RegisterForm(UserCreationForm):
    first_name = models.forms.CharField(max_length=100, required=False)
    last_name = models.forms.CharField(max_length=100, required=False)
    email = models.forms.EmailField(required=False, label='Your e-mail address')
    #message = forms.CharField(widget=forms.Textarea)
