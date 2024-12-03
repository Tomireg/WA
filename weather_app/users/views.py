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
    last_search = None  # Initialize last_search to None in case there is no previous search
    second_last_search = None  # Initialize second_last_search to None
    same_search = False  # Flag to check if the current search is the same as the last search

    if request.method == 'POST':
        form = WeatherSearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            weather_data = get_weather_data(location)

            if weather_data:
                # Save or update the last search for the user
                last_search, created = WeatherSearch.objects.update_or_create(
                    user=request.user,
                    defaults={
                        'city_name': weather_data['name'],
                        'temperature': weather_data['main']['temp'],
                        'description': weather_data['weather'][0]['description'],
                        'icon': weather_data['weather'][0]['icon'],
                        'humidity': weather_data['main']['humidity'],
                    }
                )
                # Fetch the second-to-last search
                second_last_search = WeatherSearch.objects.filter(user=request.user).exclude(id=last_search.id).order_by('-id').first()

                # Check if the current search matches the last search
                if last_search.city_name == weather_data['name']:
                    same_search = True

                # Optionally, log the result or print
                print(f"Last search created: {created}, City: {weather_data['name']}, User: {request.user.username}")
                print(f"Weather data: {weather_data}")  # Print the full weather data for debugging

                return render(request, 'users/weather_search.html', {
                    'form': form,
                    'last_search': last_search,
                    'second_last_search': second_last_search,
                    'weather_data': weather_data,
                    'same_search': same_search
                })
            else:
                # Handle if the weather data is not found
                print(f"Weather data not found for {location}")
                return render(request, 'users/weather_search.html', {'form': form, 'error': 'City not found!'})
        else:
            # Handle invalid form
            print("Form is not valid.")
    else:
        form = WeatherSearchForm()

    # Pass last_search and form to template if no POST request
    return render(request, 'users/weather_search.html', {'form': form, 'last_search': last_search, 'second_last_search': second_last_search})


# Home view
@login_required
def home(request):
    last_search = None
    if request.user.is_authenticated:
        try:
            last_search = WeatherSearch.objects.get(user=request.user)
        except WeatherSearch.DoesNotExist:
            last_search = None
    
    # Ensure we're passing both last_search and the username to the template
    return render(request, 'home.html', {'last_search': last_search, 'username': request.user.username})

