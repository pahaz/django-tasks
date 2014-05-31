from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http.response import HttpResponseRedirect

from simpleauth.forms import RegistrationForm, FormTest

# Create your views here.

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/movie')
    post = ''
    form = AuthenticationForm(None)
    if request.method == 'POST':
        post = request.POST
        form = AuthenticationForm(None, request.POST or None)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/movie')

    return render(request,  'login.html', {'form':form })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')


def registration(request):
    post = ''
    form = RegistrationForm(None)
    if request.method == 'POST':
        post = request.POST
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            user = auth.authenticate(username=post['username'],
                                     password=post['password1'])
            auth.login(request, user)


            return HttpResponseRedirect('/movie')
    return render(request,  'registration.html', {'form': form})

def account(request):
    if request.user.is_authenticated():
        user = request.user
        user_films = user.filmset.all()
        return render(request, 'account.html', {'user': user, 'user_films': user_films})
    else:
        return HttpResponseRedirect('/login')

def account_edit(request):
    user = request.user
    if user.is_authenticated():
        if request.method == 'POST':
            post = request.POST
            form = FormTest(request.POST, request.FILES, initial={'status': post['status']})
            if form.is_valid():
                if request.FILES:
                    user.avatar = request.FILES['avatar']
                if post['status']:
                    user.status = post['status']
                user.save()
            return HttpResponseRedirect(reverse('simpleauth.views.account_edit'))
        return render(request, 'edit.html')
    else:
        return HttpResponseRedirect('/login')