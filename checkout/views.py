from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request,
                       "There's nothing in your cart at the moment")
        return redirect(reverse('menu'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H5Xt4E58Eueb1mE2pevQ7hR3fIbpANqzPdcWNgNVI0G0KqlKqEdNgdAlmhKZddYYVS7e5JeowfE2THo9aHQJB5200vYlz4n8q',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
