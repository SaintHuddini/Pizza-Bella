from decimal import Decimal
from django.conf import settings
from orders.models import Recipe, Ingredient
from django.http import request



class Cart(object):
    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, food, quantity=1, override_quantity=False):
        cart = self.session.get(settings.CART_SESSION_ID)
        food_id = food.id
        if food_id not in self.cart:
            order_item = {
                'quantity': 0,
                'price': str(food.price),
            }
            self.cart[food_id] = order_item
        if override_quantity:
            self.cart[food_id]['quantity'] = quantity
        else:
            self.cart[food_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, food):
        id = food.id
        if id in self.cart:
            del self.cart[food.id]
            self.save()

    def __iter__(self):
        food_ids = self.cart.keys()
        foods = Recipe.objects.filter(id__in=food_ids)
        cart = self.cart.copy()
        for food in foods:
            cart[str(food.id)]['food'] = food
        print(cart)
            
        for item in cart.values():

            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

        

    def __len__(self):
        len = 0
        for item in self.cart.values():
            len += item['quantity'] 
        return len

    def get_total_price(self):
        total_price = 0
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

        
    def clear(self):
        
        del self.session[settings.CART_SESSION_ID]
        self.save()