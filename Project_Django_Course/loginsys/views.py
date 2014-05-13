# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            context['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', context)
    else:
        return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    context = {}
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #newuser_form.email = request.POST.get('email', '')
            #newuser_form.first_name = request.POST.get('first_name', '')
            form.save()
            new_user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
    context['form'] = form
    return render(request, 'register.html', context)