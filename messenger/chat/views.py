from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from chat.forms import RegistrationForm, InfoForm
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
import datetime
from django.core.exceptions import ObjectDoesNotExist
from chat.models import ChatUser, UserFriends, Message
import shutil

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/contacts')
    post = ''
    form = AuthenticationForm(None)
    if request.method == 'POST':
        post = request.POST
        form = AuthenticationForm(None, request.POST or None)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/contacts')

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


            return HttpResponseRedirect('/contacts')
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
        return HttpResponseRedirect(reverse('chat.views.account'))
    return render(request,  'account.html', {'user': user,
                                            'form': form})


def contacts(request):
    user = request.user
    all_friends = False
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    users = ChatUser.objects.all()
    friends = UserFriends(user.id).friend_list.all()
    if str(friends) == str(users.exclude(id=user.id)):
       all_friends = True
    knocking = []
    waiting = []
    unread = {}
    for u in users:
        if (not u in UserFriends(user.id).friend_list.all() and
            user in UserFriends(u.id).friend_list.all()):
            knocking.append(u)
        if (u in UserFriends(user.id).friend_list.all() and
            not user in UserFriends(u.id).friend_list.all()):
            waiting.append(u)
        messages_read = Message.objects.filter(to_user=user, from_user=u)
        unread[u.id] = 0
        for i in messages_read:
            if i.is_read is False:
                unread[u.id] += 1




    return render(request,  'chat/contacts.html', { 'users': users,
                                                    'user': user,
                                                    'friends': friends,
                                                    'knokings': knocking,
                                                    'waiting': waiting,
                                                    'all_friends': all_friends,
                                                    'unread': unread.items(),
                                                        })

def add_to_friends(request, name):
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    friend = ChatUser.objects.get(username=name)
    UserFriends(user.id).friend_list.add(ChatUser(friend.id))
    return HttpResponseRedirect('/contacts')

def remove_from_friends(request, name):
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    friend = ChatUser.objects.get(username=name)
    UserFriends(user.id).friend_list.remove(ChatUser(friend.id))
    UserFriends(friend.id).friend_list.remove(ChatUser(user.id))

    return HttpResponseRedirect('/contacts')

def reject(request, name):
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    friend = ChatUser.objects.get(username=name)
    UserFriends(friend.id).friend_list.remove(ChatUser(user.id))
    return HttpResponseRedirect('/contacts')


def chat_with(request, name):
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    try:
        friend = ChatUser.objects.get(username=name)
    except ObjectDoesNotExist:
         return HttpResponseRedirect('/contacts')
    if (not friend in UserFriends(user.id).friend_list.all() or
         not user in UserFriends(friend.id).friend_list.all()):
        return HttpResponseRedirect('/contacts')
    messages_read = Message.objects.filter(to_user=user, from_user=friend)
    for mes in messages_read:
        mes.is_read = True
        mes.save()
    if request.method == 'POST':
        post = request.POST

        m = Message(
            message=post['message'],
            from_user=user,
            to_user=friend,
            datetime=datetime.datetime.today()
            )
        m.save()
    messages = Message.objects.filter(to_user=friend, from_user=user) |\
               Message.objects.filter(to_user=user, from_user=friend)


    return render(request,  'chat/chat.html', {'user': user,
                                               'friend': friend,
                                               'messages': messages})


def unread_with(request, name):
    user = request.user
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    try:
        friend = ChatUser.objects.get(username=name)
    except ObjectDoesNotExist:
         return HttpResponseRedirect('/contacts')
    messages_read = Message.objects.filter(to_user=user, from_user=friend)
    unread = 0
    for i in messages_read:
        if i.is_read is False:
            unread += 1



    return render(request,  'chat/unread.html', {'user': user,
                                               'friend': friend,
                                               'unread': unread
                                               })
