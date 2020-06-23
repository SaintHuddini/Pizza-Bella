

def cart_contents(request):

    cart_items = []
    total = 0
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