from django.urls import path
from . import views 
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name = "list-home"),
    path("about",views.about, name = "list-about"),
    path('register', user_views.register, name = "register"),

    #På dessa använder vi class based views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('profile',user_views.profile, name = 'user-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
