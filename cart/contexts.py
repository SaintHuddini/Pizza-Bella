"""
Contexts for the cart that is available everywhere in the website
"""
from django.shortcuts import get_object_or_404
from orders.models import Recipe


def cart_contents(request):
    """
    Cart logic of prices, items and quantity
    """
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    item_count = 0

    for item_id, quantity in cart.items():
        food = get_object_or_404(Recipe, pk=item_id)
        total += quantity * food.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'food': food,
        })
    if total == 0:
        delivery = 0
    else:
        delivery = 2
    grand_total = delivery + total
    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }
    return context
