from django import forms
from .models import Recipe, Category


class FoodForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
      
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'