"""
Models of the food menu
"""
from django.db import models


class Recipe(models.Model):
    """
    Pizza, Pasta, Salad, Kebab and Hamburger
    """
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=124, blank=True)
    category = models.CharField(max_length=32, default='PIZZA', choices=(
        ('PIZZA', 'Pizza'), ('HAMBURGER', 'Hamburger'),
        ('SALAD', 'Salad'), ('PASTA', 'Pasta'),
        ('KEBAB', 'Kebab')))
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
