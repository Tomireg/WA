from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, WeatherSearchForm
from .models import WeatherSearch
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings

# Function to fetch weather data from OpenWeatherMap
def get_weather_data(location):
    api_key = settings.OPENWEATHERMAP_API_KEY  # It's better to store your API key in settings.py
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    url = f'{base_url}?q={location}&appid={api_key}&units=metric'  # Using metric to get temperature in Celsius
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the weather data as JSON
    return None  # If the API request fails, return None

# Custom logout view
def custom_logout(request):
    logout(request)
    return render(request, 'users/logout.html')

# Register view to handle user registration
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

# Weather search view to search for weather data
@login_required
def weather_search(request):
    form = WeatherSearchForm(request.POST or None)
    weather_data = None

    if form.is_valid():
        location = form.cleaned_data['location']
        weather_data = get_weather_data(location)  # Fetch weather data

        if weather_data:
            # Save the weather search in the database
            WeatherSearch.objects.create(
                user=request.user,
                location=location,
                temperature=weather_data['main']['temp'],
                description=weather_data['weather'][0]['description'],
                humidity=weather_data['main']['humidity']
            )

    return render(request, 'users/weather_search.html', {'form': form, 'weather_data': weather_data})

# Home view to display the last weather search
@login_required
def home(request):
    # Get the logged-in user's username
    username = request.user.username

    # Get the last weather search for the user
    last_weather_search = WeatherSearch.objects.filter(user=request.user).order_by('-date_searched').first()

    return render(request, 'home.html', {
        'username': username,
        'last_weather_search': last_weather_search
    })