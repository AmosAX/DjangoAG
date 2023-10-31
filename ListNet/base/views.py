from django.shortcuts import render
from django.http import HttpResponse

from . models import List


'''
lists = [
        {
        'title': 'List1',
        'content' : 'Java'
    },
        {
        'title': 'List2',
        'content':'Python'
    }
]
'''

# Create your views here.
def home(request):

    context = {
        'lists' : List.objects.all()
    }
    return render(request,"base/home.html",context)


def about(request):
    return render(request,"base/about.html")