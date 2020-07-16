from django.contrib import admin
from .models import Recipe, Ingredient, OrderItem, CartOrder, Payments
# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'order_item_state',
    )
class CartOrderAdmin(admin.ModelAdmin):
    list_display = (
        'time',
        'total_price',
        'customer',
    )

admin.site.register(Payments)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(OrderItem, OrderAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
