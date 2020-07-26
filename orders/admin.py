"""
Recipe Admin Registration
"""
from django.contrib import admin
from .models import Recipe
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    """
    Fixing a custom admin panel
    """
    list_display = (
        'name',
        'category',
        'price',
    )


admin.site.register(Recipe, RecipeAdmin)
