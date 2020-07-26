"""Menu, Homepage and Foodpages urls"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/pizza/', views.pizza_menu, name='pizza_menu'),
    path('add/', views.add_food, name='add_food'),
    path('edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
    path('menu/', views.menu, name='menu'),
    path('menu/pasta', views.pasta_menu, name='pasta_menu'),
    path('menu/salad', views.salad_menu, name='salad_menu'),
    path('menu/hamburger', views.hamburger_menu, name='hamburger_menu'),
    path('menu/kebab', views.kebab_menu, name='kebab_menu'),
]
