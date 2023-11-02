from django.shortcuts import render
from django.http import HttpResponse


#Class based views imports
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


#Vi importerar in från Models List klassen
from .models import List

#Kom ihåg att importera mixes 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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

## OBS ATT SÄNDA IN MIXIN FÖRST
class PostCreatView(LoginRequiredMixin,CreateView):

    #när vi använderMixin kom ihåg att fixa settings
    #KOLLA SETTINGS
    #LOGIN_URL = '/account/login/'
    model = List
    fields = ['title','content']

    #gör en overide för att sätta in våran author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    #när vi använderMixin kom ihåg att fixa settings
    #KOLLA SETTINGS
    #LOGIN_URL = '/account/login/'
    model = List
    fields = ['title','content']

    #gör en overide för att sätta in våran author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #Funktion som kollar om user för posten och usern som är inloggad är samma
    def test_func(self):
        List = self.get_object()
        if self.request.user == List.author:
            return True;
    
    #
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    #vi använder List inte post i models
    model = List

    #Delete kommer inte fungera om den inte vet var den ska sända folk om det lyckas
    success_url = '/'


    def test_func(self):
        List = self.get_object()
        if self.request.user == List.author:
            return True;


def about(request):
    return render(request, 'base/about.html')
