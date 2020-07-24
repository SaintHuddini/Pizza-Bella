from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages

from orders.models import Recipe


def view_cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    food = get_object_or_404(Recipe, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request, f'Updated {food.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {food.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):

    food = get_object_or_404(Recipe, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {food.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(
            request, f'removed {food.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    food = get_object_or_404(Recipe, pk=item_id)
    cart = request.session.get('cart', {})

    print(item_id)
    cart.pop(str(item_id))
    messages.success(
        request, f'removed {food.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
