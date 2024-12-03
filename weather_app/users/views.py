from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, WeatherSearchForm
from .models import WeatherSearch
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


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
    last_search = None
    second_last_search = None

    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            weather_data = get_weather_data(location)

            if weather_data:
                # Save the new search
                last_search = WeatherSearch.objects.create(
                    user=request.user,
                    city_name=weather_data['name'],
                    temperature=weather_data['main']['temp'],
                    description=weather_data['weather'][0]['description'],
                    icon=weather_data['weather'][0]['icon'],
                    humidity=weather_data['main']['humidity'],
                )

                # Fetch the second-to-last search
                second_last_search = WeatherSearch.objects.filter(user=request.user).exclude(id=last_search.id).order_by('-search_date').first()

                return render(request, 'users/weather_search.html', {
                    'form': form,
                    'last_search': last_search,
                    'second_last_search': second_last_search,
                    'weather_data': weather_data,
                })
            else:
                # Handle if the weather data is not found
                return render(request, 'users/weather_search.html', {'form': form, 'error': 'City not found!'})
        else:
            # Handle invalid form
            pass
    else:
        form = WeatherSearchForm()

    return render(request, 'users/weather_search.html', {'form': form, 'last_search': last_search, 'second_last_search': second_last_search})


# Home view
@login_required
def home(request):
    return render(request, 'home.html', {'username': request.user.username})