from django.contrib import admin
from django.urls import path, include
from .views import home, pizza_menu, add_food, edit_food, delete_food, hamburger_menu, kebab_menu, menu, pasta_menu, salad_menu

urlpatterns = [
    path('', home, name='home'),
    path('menu/pizza/', pizza_menu, name='pizza_menu'),
    path('add/', add_food, name='add_food'),
    path('edit/<int:food_id>/', edit_food, name='edit_food'),
    path('delete/<int:food_id>/', delete_food, name='delete_food'),
    path('menu/', menu, name='menu'),
    path('menu/pasta', pasta_menu, name='pasta_menu'),
    path('menu/salad', salad_menu, name='salad_menu'),
    path('menu/hamburger', hamburger_menu, name='hamburger_menu'),
    path('menu/kebab', kebab_menu, name='kebab_menu'),
]
