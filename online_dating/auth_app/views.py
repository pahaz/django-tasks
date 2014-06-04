from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user:
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def auth_only(request):
	return render_to_response('auth_app/auth_only.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'auth_app/register_success.html', {})
	else:
		form = UserCreationForm()
	return render(request, 'auth_app/register.html', {'form' : form})