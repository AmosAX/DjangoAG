from django.urls import path
#. i import visar att det är en lokal import och vi behöver views filen med våra definerade funktioner
from . import views

#Namn list-home kanske verkar lite väl definerat men det är bra kodvana att definera ordentligt så ifall vi skulle ha flera appar att v inte får problem med namn, 
#list-home. user-home etc
urlpatterns = [
    path('', views.home, name='list-home'),
    path("about", views.about, name = 'list-about')
]