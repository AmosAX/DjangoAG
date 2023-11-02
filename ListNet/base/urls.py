from django.urls import path
from . import views 
from users import views as user_views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

##Det vi importerar in för class based views från våra views
from .views import PostListView,PostDetailView,PostCreatView,PostUpdateView,PostDeleteView



urlpatterns = [

    #path("", views.home, name = "list-home"),
    #Kom ihåg att förklara PostListView as view
    path("", PostListView.as_view(), name = "list-home"),

    #Vi skapar en URL pattern för speficik post som tar in en variabel!! observera namnet
    path('list/<int:pk>/', PostDetailView.as_view(), name='list-detail'),
    #
    path('list/new/', PostCreatView.as_view(), name='list-create'),

    path('list/<int:pk>/update', PostUpdateView.as_view(), name='list-update'),

    #förväntar sig en template om vi är säkra på att vi ska deletea
    path('list/<int:pk>/delete', PostDeleteView.as_view(), name='list-delete'),


    path("about",views.about, name = "list-about"),
    path('register', user_views.register, name = "register"),

    #På dessa använder vi class based views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('profile',user_views.profile, name = 'user-profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
