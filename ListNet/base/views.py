from django.shortcuts import render
from django.http import HttpResponse


#Vi importerar in från Models List klassen
from .models import List

"""
lists = [
    {
        'author': 'Amos',
        'title': 'Lista 1',
        'content': 'Java',
    },
    {
        'author': 'Amos',
        'title': 'Lista 2',
        'content': 'Python',
    }
]
Vi kommenterar bort våran exempel data 
"""
# Create your views here.
def home(request):
    context = {
        'posts': List.objects.all()
    }
    return render(request, 'base/home.html', context)

def about(request):
    return render(request, 'base/about.html')