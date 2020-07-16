from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Ingredient(models.Model):
    name         = models.CharField(max_length=32)
    price        = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

class Recipe(models.Model):
    name          = models.CharField(max_length=32)
    description   = models.TextField(max_length=124, blank=True)
    category      = models.CharField(max_length=32, default='PIZZA', choices= (('PIZZA', 'Pizza'), ('HAMBURGER', 'Hamburger'), ('SALAD', 'Salad'), ('PASTA', 'Pasta'), ('KEBAB', 'Kebab')))
    price         = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f'{self.name}'



class Payments(models.Model):
   
    class Meta:
        verbose_name_plural = 'Payments'

    payment_state      = models.CharField(max_length=32, default='PENDING', choices= (('PENDING', 'Pending'), ('RECEIVED', 'Received'), ('FAILURE', 'Failure')))
    gateway = models.CharField(max_length=48, null=True, default='Credit', choices= (('CREDIT', 'Credit'), ('STRIPE', 'Stripe')))

    def __str__(self):
        return f'{self.payment_state}'


class CartOrder(models.Model):
     

    time          = models.DateTimeField(default=timezone.now)
    total_price   = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    cart_state      = models.CharField(max_length=32, default='PENDING', choices= (('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering'))) 
    payment       = models.ForeignKey(Payments, on_delete=models.PROTECT, blank=False, default=1)
    customer      = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self): 
        return f'{self.total_price}'

class OrderItem(models.Model):
    food          = models.ForeignKey(Recipe, on_delete=models.PROTECT, null=True)
    cart          = models.ForeignKey(CartOrder, on_delete=models.CASCADE, null=True)
    extra         = models.ManyToManyField(Ingredient, blank=True)
    price         = models.DecimalField(decimal_places=2, max_digits=4, null=True) 
    quantity = models.IntegerField(default=1)
    order_item_state      = models.CharField(max_length=32, default='PENDING', choices= (('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering'))) 
    
    def __str__(self):
        return f'{self.foods}'
