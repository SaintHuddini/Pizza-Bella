from django.shortcuts import render, redirect
from .models import Recipe
# Create your views here.

pizza = Recipe.objects.filter(category='PIZZA')
hamburger = Recipe.objects.filter(category='HAMBURGER')
pasta = Recipe.objects.filter(category='PASTA')
salad = Recipe.objects.filter(category='SALAD')
kebab = Recipe.objects.filter(category='KEBAB')

def home(request):
    return render(request, 'orders/home.html')

def menu(request):
    context = {
        'pizza': pizza,
        'kebab': kebab,
        'pasta': pasta,
        'salad': salad,
        'hamburger': hamburger,
    }
    return render(request, 'orders/menu.html', context)