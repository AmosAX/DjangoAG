from django.shortcuts import render
from django.http import HttpResponse

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

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def about(request):
    return HttpResponse('This is the about page')