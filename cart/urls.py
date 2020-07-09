from django.urls import path, include, re_path
from .views import cart_detail, cart_add, cart_remove

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:food_id>', cart_add, name='cart_add'),
    path('remove/<int:id>', cart_remove, name='cart_remove'),
]
