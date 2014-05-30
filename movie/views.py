from django.shortcuts import render
from movie.models import Movie, User
from django.http.response import HttpResponseRedirect
from movie.forms import RegistrationForm, FormTest
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib import auth
from movie.models import Pay
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render

def movie_list(request):
    if request.user.is_authenticated():
        items = Movie.objects.all()
        ymovie =  request.user.filmset.all()
        return render(request, 'movie/index.html', {'items': items, 'your_movies': ymovie})
    else:
        return HttpResponseRedirect('/login')

def movie(request, id):
    if request.user.is_authenticated():
        check = False
        info = {}
        list_info = []
        ymovie =  request.user.filmset.all()
        for i in ymovie:
            list_info.append(i.id)
        if int(id) in list_info:
            check = True
        else:
            check = False
        info['movies'] = get_object_or_404(Movie, id=id)
        info['username'] = request.user.username
        info['proof'] = check
        return render(request, 'movie/movie.html', info)
    else:
        return HttpResponseRedirect('/login')

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
            return HttpResponseRedirect(reverse('movie.views.account_edit'))
        return render(request, 'edit.html')
    else:
        return HttpResponseRedirect('/login')

def buy(request, id):
    check = False
    buy = {}
    list_info = []
    ymovie =  request.user.filmset.all()
    for i in ymovie:
        list_info.append(i.id)
    if int(id) in list_info:
        check = True
    else:
        check = False
    buy['user'] = request.user
    buy['movies'] = Movie.objects.get(id=id)
    buy['proof'] = check
    return render(request, 'movie/buy.html', buy)

def thanks(request):
    check = False
    if request.method == 'POST':
        listfilms = []
        movieid = request.POST['Films']
        movieobj = Movie.objects.get(id=movieid)
        user = request.user
        for i in user.filmset.all():
            listfilms.append(i.id)
        print movieid
        print listfilms
        if int(movieid) in listfilms:
            return HttpResponseRedirect('/movie') # redirect to your movies catalog
        else:
            user.balance -= movieobj.price
            user.filmset.add(movieobj)
            user.save()
            return HttpResponseRedirect('/movie')
    else:
        return HttpResponseRedirect('/movie')

def paypage(request):
    if request.user.is_authenticated():
        return render(request, 'pay.html')
    else:
        return HttpResponseRedirect('/login')

def pay(request):
    if request.method == 'POST':
        howmany = int(request.POST['pay'])
        user = request.user
        user.balance += int(howmany)
        user.save()
        return HttpResponseRedirect('/movie')

