from django import forms
from .models import Recipe, Ingredient, OrderItem

class FoodForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['foods', 'extra', ]
