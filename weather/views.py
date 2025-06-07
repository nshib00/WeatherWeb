from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from requests import JSONDecodeError

from weather.forms import CityForm
from weather.models import City
from .services.weather_api import WeatherAPIService


@login_required
def home(request: HttpRequest) -> HttpResponse:
    initial_city = request.session.pop('last_city', None)
    weather_data = None
    error = None

    if initial_city:
        weather_data = WeatherAPIService.get_today_weather(initial_city)

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


@login_required
def favorite_cities(request: HttpRequest) -> HttpResponse:
    cities = City.objects.filter(user=request.user).order_by('-is_default', 'name')
    return render(request, 'weather/favorite.html', context={'cities': cities})


@login_required
def add_favorite_city(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        full_city_name = request.POST.get('city')

        if full_city_name:
            try:
                city, region = [part.strip() for part in full_city_name.split(',', 1)]

                if not City.objects.filter(user=request.user, name=city).exists():
                    City.objects.create(user=request.user, name=city, region=region, is_default=False)
                    messages.success(request, f"Город {city} добавлен в избранные.")
                else:
                    messages.warning(request, f"Город {city} уже в избранных.")                
            except (ValueError, JSONDecodeError):
                messages.error(request, "Невозможно определить город и регион. Проверьте, правильно ли написано название города.")
        else:
            messages.error(request, "Название города не передано.")

        request.session['last_city'] = full_city_name

    return redirect('home')


@login_required
def set_default_city(request: HttpRequest) -> HttpResponse:
    pass


@login_required
def delete_favorite_city(request: HttpRequest, id: int) -> HttpResponse:
    pass
