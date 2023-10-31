from django.shortcuts import render
from django.http import HttpResponse


#Class based views imports
from django.views.generic import ListView,DetailView,CreateView



#Vi importerar in från Models List klassen
from .models import List

# Create your views here.
def home(request):
    context = {
        'lists': List.objects.all()
    }
    return render(request, 'base/home.html', context)


#CLASS INTE DEF
#för när vi ser på flera posts
class PostListView(ListView):
    #vi använder List inte post i models
    model = List
    template_name = 'base/home.html'
    context_object_name = 'lists'
    ordering = ['date_posted']


#bara för en specific post, kom ihåg att göra URL pattern
class PostDetailView(DetailView):
    #vi använder List inte post i models
    model = List

class PostCreatView(CreateView):
    model = List
    fields = ['title','content']

    #gör en overide för att sätta in våran author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'base/about.html')
