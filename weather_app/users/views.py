from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
import requests
from .forms import WeatherSearchForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def weather_search(request):
    form = WeatherSearchForm()
    weather_data = None

    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            api_key = 'e16aae9246a1a91b85dcbba7ee8d64ae'  # Replace with your OpenWeatherMap API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()

    return render(request, 'users/weather_search.html', {'form': form, 'weather_data': weather_data})