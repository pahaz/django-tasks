from django.shortcuts import render
from django.http.response import HttpResponseRedirect
# Create your views here.

def index_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/movie')
    else:
        return render(request, 'index.html')

