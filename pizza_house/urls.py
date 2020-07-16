"""pizza_house URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from orders.views import menu, hamburger_menu, kebab_menu, pasta_menu, pizza_menu, salad_menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls')),
    path('', include('orders.urls')),
    path('menu/', menu, name='menu'),
    path('menu/pasta', pasta_menu, name='pasta_menu'),
    path('menu/salad', salad_menu, name='salad_menu'),
    path('menu/hamburger', hamburger_menu, name='hamburger_menu'),
    path('menu/kebab', kebab_menu, name='kebab_menu'),

]
