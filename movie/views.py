from django.http.response import HttpResponseRedirect
from movie.models import Movie
from django.shortcuts import get_object_or_404, render

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

