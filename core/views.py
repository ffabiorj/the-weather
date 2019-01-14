from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.contrib import messages

def home(request):
    """
    
    """
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=36a83bb3097fd2cad04a91b0bfe6b45c'
    cities = City.objects.all()
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        messages.success(request, 'A cidade foi adicionada com sucesso!')
    
    form = CityForm()

    for city in cities:
        r = requests.get(url.format(city)).json()
        temp_weather = {
            'id': city.id,
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(temp_weather)
    context = {
        'temp_weather': weather_data, 'form': form,
        }
    return render(request, 'index.html', context)

def delete_weather(request, id):
    """Delete a city by id."""
    weather = City.objects.get(id=id)
    weather.delete()
    messages.success(request, 'A cidade foi deletada com sucesso!')
    return redirect(home)
