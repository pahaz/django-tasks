from django.template import RequestContext
from django.shortcuts import render_to_response
from music.models import Track, UserProfile, HistoryEntity
from music.forms import RegisterForm, LoginForm
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime


def all_tracks(request):
    context = RequestContext(request)
    tracks = Track.objects.all()
    context_dict = {
        'trackListType': 'all',
        'username': request.user.username,
        'tracksJson': tracks.values(),
        'tracks': tracks
    }
    return render_to_response('music/trackList.html', context_dict, context)


@login_required
def history(request):
    context = RequestContext(request)
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    tracks = get_last_tracks_of_history(user_profile)
    tracks = set_dates(tracks, user_profile)
    context_dict = {
        'trackListType': 'history',
        'username': user.username,
        'tracksJson': tracks.values(),
        'tracks': tracks
    }
    return render_to_response('music/trackList.html', context_dict, context)


def get_last_tracks_of_history(user_profile):
    track_history = Track.objects.filter(historyentity__user_profile=user_profile)
    track_history = track_history.order_by('-historyentity__listen_date')
    return track_history[:user_profile.history_size]


def set_dates(tracks, user_profile):
    for track in tracks:
        date = HistoryEntity.objects.get(track=track, user_profile=user_profile).listen_date
        track.listen_date = date
    return tracks


def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.set_password(user.password)
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            print("Зарегистрирован новый пользователь: " + user.username)
            registered = True
        else:
            print(register_form.errors)
    else:
        register_form = RegisterForm()
    if not registered:
        return render_to_response(
            'music/logReg.html',
            dict(register_form=register_form, login_form=LoginForm(), registered=registered),
            context)
    else:
        return log_in(request)


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print("Пользователь " + username + " выполнил вход")
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Ваш аккаунт заблокирован")
        else:
            print("Неудачная попытка входа: {0}, {1}".format(username, password))
            return HttpResponse("Не удалось выполнить вход с вашими данными")
    else:
        return HttpResponseRedirect('/register')


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def push_to_history(request):
    user = request.user
    track_url = request.GET['track_url']
    track = Track.objects.get(url=track_url)
    user_profile = UserProfile.objects.get(user=user)
    history_add(user_profile, track)
    return HttpResponse()


def history_add(user_profile, track):
    tracks = get_last_tracks_of_history(user_profile)
    if not contains(tracks, track):
        history_entity = HistoryEntity(user_profile=user_profile,
                                       track=track,
                                       listen_date=datetime.now())
    else:
        history_entity = HistoryEntity.objects.get(user_profile=user_profile,
                                                   track=track)
        history_entity.listen_date = datetime.now()
    history_entity.save()
    return HttpResponse()


def contains(query_set, elem):
    for e in query_set:
        if e.id == elem.id:
            return True
    return False