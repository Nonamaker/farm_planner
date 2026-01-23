from django import forms

from stock.models import Chicken, LiveStock


class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = ["dob", "dod", "sex"]


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ["band_color", "band_number", "breed", "mature_age"]