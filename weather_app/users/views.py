from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
import requests
from .forms import WeatherSearchForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
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
            api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()

    return render(request, 'users/weather_search.html', {'form': form, 'weather_data': weather_data})