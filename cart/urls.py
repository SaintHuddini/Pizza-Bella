from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<int:item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
