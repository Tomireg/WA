from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from .views import weather_search
from users import views as user_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.custom_logout, name='logout'),
    path('weather/', weather_search, name='weather_search'),
]