from django.urls import path, include
from .views import view_cart
urlpatterns = [
    path('', view_cart, name='view_cart'),
]
