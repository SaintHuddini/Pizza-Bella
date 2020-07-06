from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from orders.models import Recipe
from .cart import Cart
from .forms import CartAddFoodForm
from django.http import HttpResponse
# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

@require_POST
def cart_add(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Recipe, pk=food_id)
    form = CartAddFoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(food=food, quantity=cd['quantity'], override_quantity=cd['override'])
        return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, food_id):
    cart = Cart(request)
    food = get_object_or_404(Recipe, id=food_id)
    cart.remove(food)
    return redirect('cart:cart_detail')



