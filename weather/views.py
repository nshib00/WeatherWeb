from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from weather.forms import CityForm
from .services.weather_api import WeatherAPIService


def home(request: HttpRequest) -> HttpResponse:
    weather_data = None
    error = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = WeatherAPIService.get_today_weather(city)
            if not weather_data:
                error = "Город не найден." 
    else:
        form = CityForm()

    context = {
        'form': form,
        'weather_data': weather_data, 
        'error': error,
        'title': 'Погода на сегодня'
    }
    return render(request, 'weather/home.html', context)