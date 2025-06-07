from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('favorite', views.favorite_cities, name='favorites'),
    path('favorite/add', views.add_favorite_city, name='add_favorite_city'),
    path('favorite/set-default/<int:id>', views.set_default_city, name='set_default_city'),
    path('favorite/delete/<int:id>', views.delete_favorite_city, name='delete_favorite_city'),
]