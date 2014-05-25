from django.shortcuts import render
from movie.models import Movie
from django.http.response import HttpResponseRedirect
from movie.forms import RegistrationForm, InfoForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib import auth


def movie_list(request):
    items = Movie.objects.all()
    return render(request, 'movie/index.html', {'items': items})

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
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    form = InfoForm(initial={'status': user.status})
    if request.method == 'POST':
        post = request.POST
        form = InfoForm(request.POST, request.FILES, initial={'status': post['status']})
        if form.is_valid():
            if request.FILES:
                user.avatar = request.FILES['avatar']
            if post['status']:
                user.status = post['status']
            user.save()
        return HttpResponseRedirect(reverse('movie.views.account'))
    return render(request,  'account.html', {'user': user,
                                            'form': form})