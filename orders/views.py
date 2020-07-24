from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe
from django.http import HttpResponse
from .forms import FoodForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def home(request):
    return render(request, 'orders/home.html')


def menu(request):
    return render(request, 'orders/menu.html')


def pizza_menu(request):
    pizza = Recipe.objects.filter(category='PIZZA')
    context = {
        'pizza': pizza,
    }
    return render(request, 'orders/pizza.html', context)


def kebab_menu(request):
    kebab = Recipe.objects.filter(category='KEBAB')
    context = {
        'kebab': kebab,
    }
    return render(request, 'orders/kebab.html', context)


def salad_menu(request):
    salad = Recipe.objects.filter(category='SALAD')
    context = {
        'salad': salad,
    }
    return render(request, 'orders/salad.html', context)


def pasta_menu(request):
    pasta = Recipe.objects.filter(category='PASTA')
    context = {
        'pasta': pasta,
    }
    return render(request, 'orders/pasta.html', context)


def hamburger_menu(request):
    hamburger = Recipe.objects.filter(category='HAMBURGER')
    context = {
        'hamburger': hamburger,
    }
    return render(request, 'orders/hamburger.html', context)


@login_required
def add_food(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Add a product to the store """
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_food'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = FoodForm()

    template = 'orders/add_food.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_food(request, food_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Edit a product in the store """
    food = get_object_or_404(Recipe, pk=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Food!')
            return redirect(reverse('menu'))
        else:
            messages.error(
                request, 'Failed to update food item. Please ensure the form is valid.')
    else:
        form = FoodForm(instance=food)
        messages.info(request, f'You are editing {food.name}')

    template = 'orders/edit_food.html'
    context = {
        'form': form,
        'food': food,
    }

    return render(request, template, context)


@login_required
def delete_food(request, food_id):
    """ Delete a food from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    food = get_object_or_404(Recipe, pk=food_id)
    print(food)
    food.delete()
    messages.success(request, 'Food deleted!')
    return redirect(reverse('menu'))
