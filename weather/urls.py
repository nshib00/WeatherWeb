from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('favorite', views.favorite_cities, name='favorites'),
    path('favorite/add', views.add_favorite_city, name='add_favorite_city'),
]