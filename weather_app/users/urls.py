from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, search_weather, home, custom_logout

urlpatterns = [
    path('', home, name='home'),  # Home view as the default landing page
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('weather/', search_weather, name='weather_search'),
]
