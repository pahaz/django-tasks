from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    err_msg = dict(invalid="Имя содержит недопустимые символы",
                   required="Введите имя",
                   unique="Пользователь с таким именем уже зарегистрирован")
    username = forms.CharField(label='Имя пользователя',
                               error_messages=err_msg,
                               max_length=30)
    err_msg = dict(invalid="Пароль содержит недопустимые символы",
                   required="Введите пароль")
    password = forms.CharField(label='Пароль',
                               error_messages=err_msg,
                               widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterForm(LoginForm):
    err_msg = dict(invalid="email введён некорректно (да он и не обязателен, можете оставить поле пустым)")
    email = forms.CharField(label='Email',
                            required=False,
                            error_messages=err_msg,
                            max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')