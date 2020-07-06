from django import forms

ORDER_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 20)]


class CartAddFoodForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=ORDER_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
