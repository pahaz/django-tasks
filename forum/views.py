from django.shortcuts import render, get_object_or_404
from forum.models import Theme, Message
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.views import generic
from forum.forms import LoginForm, RegisterForm, EditForm
from django import forms
from django.core.paginator import Paginator


class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'themes'

    def get_queryset(self):
        themes = Theme.objects.order_by('created')
        paginator = Paginator(themes, 10)
        page=self.request.path[1:]
        if page == '':
            page = 1
        try:
            ret_themes = paginator.page(page)
        except:
            ret_themes = ''
        return ret_themes


class DetailsView(generic.DetailView):
    model = Theme
    template_name = 'forum/theme_mess.html'


class LoginView(generic.FormView):
    template_name = 'forum/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.clean()['username']
        password = form.clean()['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            request = self.request
            login(request, user)
            return HttpResponseRedirect(reverse('forum:index'))


class RegisterView(generic.CreateView):
    template_name = 'forum/register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        username = form.clean_username()
        password = form.clean_password2()

        user_f = User.objects.create_user(username=username,
                                          password=password,
                                          )
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('forum:index'))


def add_message(request, pk):
    if request.user != None:
        try:
            message = request.POST['new_message_text']
        except:
            message = ''
        if message != '':
            new_message = Message(theme=Theme.objects.get(pk=pk), text=message, created=timezone.now(), author=request.user)
            new_message.save()
            return HttpResponseRedirect(reverse('forum:theme_mess', args=(pk, )))
    return HttpResponseRedirect(reverse('forum:theme_mess', args=(pk, )))


def add_theme(request):
    if request.user != None:
        try:
            theme = request.POST['new_theme_name']
        except:
            theme = ''
        if theme != '':
            new_theme = Theme(name=theme, created=timezone.now(), author=request.user)
            new_theme.save()
            return HttpResponseRedirect(reverse('forum:theme_mess', args=(new_theme.pk, )))
    return HttpResponseRedirect(reverse('forum:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('forum:index'))


def delete_message(request, tpk, mpk):
    if request.user == Message.objects.filter(pk=mpk)[0].author:
        Message.objects.filter(pk=mpk).delete()
    return HttpResponseRedirect(reverse('forum:theme_mess', args=(tpk, )))


def edit_mess_page(request, tpk, mpk):
    if request.user == Message.objects.filter(pk=mpk)[0].author:
        text = Message.objects.filter(pk=mpk)[0].text
        mess = Message.objects.filter(pk=mpk)[0]
        form = EditForm(request.POST or None, initial={'message': text})
        if request.method == 'POST' and form.is_valid():
            mess.text = form.cleaned_data.get('message')
            mess.save()
            return HttpResponseRedirect(reverse('forum:theme_mess', args=(tpk, )))

        context = {'form': form, 'tpk': tpk, 'mpk': mpk, 'text': text}
        return render(request, 'forum/edit_mess.html', context)
    return HttpResponseRedirect(reverse('forum:theme_mess', args=(tpk, )))