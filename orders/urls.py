from django.contrib import admin
from django.urls import path, include
from .views import home, pizza_menu, add_food

urlpatterns = [
    path('', home, name='home'),
    path('menu/pizza/', pizza_menu, name='pizza_menu'),
    path('add/', add_food, name='add_food'),
]
