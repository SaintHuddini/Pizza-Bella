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

class PaymentState(models.Model):

    status = models.CharField(max_length=48, null=False, blank=False, default='PENDING')

    def __str__(self):
        return f'{self.status}'


class OrderItem(models.Model):
    foods         = models.ManyToManyField(Recipe)
    extra         = models.ManyToManyField(Ingredient, blank=True)
    price         = models.DecimalField(decimal_places=2, max_digits=4, null=True) 
    order_item_state      = models.CharField(max_length=32, default='PENDING', choices= (('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering'))) 
    
    def __str__(self):
        return f'{self.foods}'


class Payments(models.Model):
   
    class Meta:
        verbose_name_plural = 'Payments'

    state = models.ForeignKey(PaymentState, on_delete=models.PROTECT, default=0)
    gateway = models.CharField(max_length=48, null=False, default='Credit')

    def __str__(self):
        return f'{self.status}'


class CartOrder(models.Model):
     

    items         = models.ManyToManyField(OrderItem)
    time          = models.DateTimeField(default=timezone.now)
    total_price   = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    cart_state      = models.CharField(max_length=32, default='PENDING', choices= (('PENDING', 'Pending'), ('PROCCESSING', 'Proccessing'), ('DELIVERING', 'Delivering'))) 
    payment       = models.ForeignKey(Payments, on_delete=models.PROTECT, blank=False, default=0)
    customer      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self): 
        return f'{self.items}'