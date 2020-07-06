from django.contrib import admin
from django.urls import path, include
from .views import home, pizza_order, pizza_menu
urlpatterns = [
    path('', home, name='home'),
    path('menu/pizza/', pizza_menu, name='pizza_menu'),
    path('menu/pizza/<int:order_id>', pizza_order, name='pizza_order' )
]
