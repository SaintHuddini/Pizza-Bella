

from cart.cart import Cart

def cart_contents(request):

    cart = Cart(request)
    
    total = cart.get_total_price()
    product_count = 0
    delivery = 0
    grand_total = delivery + total 

    if total > 0:
        delivery = 0
    else:
        delivery = 2

    contexts = {
    'total': total,
    'grand_total': grand_total,
    'product_count':product_count,
    'delivery':delivery,
    }

    return contexts