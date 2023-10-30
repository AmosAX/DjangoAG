from django.urls import path
#. i import visar att det är en lokal import och vi behöver views filen med våra definerade funktioner
from . import views

#Vi måste börja med att importa lite saker, notera att vi har två views så AS keyworded är viktigt
from django.contrib.auth import views as auth_views

from users import views as user_views


urlpatterns = [
    path('', views.home, name='list-home'),
    path("about", views.about, name = 'list-about'),
    path('register',user_views.register, name = 'register'),


    #Vi kan använda oss av vårt senaste import, obs att vi måste skapa våra templates om vi inte redan gjort det
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]