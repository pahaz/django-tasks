from django.shortcuts import render
from models import MovieField
# Create your views here.

def index(request):
    items = MovieField.objects.all()
    return render(request, 'films/index.html', {'items':items})

def main(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts/index.html')