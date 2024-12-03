from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, WeatherSearchForm
from .models import LastWeatherSearch
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

# Fetch weather data
def get_weather_data(location):
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    url = f'{base_url}?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {'error': 'City not found!'}
    else:
        return {'error': 'Error fetching weather data. Please try again later.'}

# Custom logout
def custom_logout(request):
    logout(request)
    return redirect('login')

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Weather search view
@login_required
def search_weather(request):
    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            weather_data = get_weather_data(location)

            if weather_data:
                # Save or update the last search for the user
                LastWeatherSearch.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'city_name': weather_data['name'],
                        'temperature': weather_data['main']['temp'],
                        'description': weather_data['weather'][0]['description'],
                        'icon': weather_data['weather'][0]['icon'],
                        'humidity': weather_data['main']['humidity'],
                    }
                )
                # Ensure we're returning a standard HTTP response
                return render(request, 'users/weather_search.html', {'weather_data': weather_data})
            else:
                return render(request, 'users/weather_search.html', {'error': 'City not found!'})
    else:
        form = WeatherSearchForm()

    return render(request, 'users/weather_search.html', {'form': form})

# Home view
@login_required
def home(request):
    last_search = None
    if request.user.is_authenticated:
        try:
            last_search = LastWeatherSearch.objects.get(user=request.user)
        except LastWeatherSearch.DoesNotExist:
            last_search = None
    
    # Ensure we're passing both last_search and the username to the template
    return render(request, 'home.html', {'last_search': last_search, 'username': request.user.username})

