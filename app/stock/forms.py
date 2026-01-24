from django import forms

from stock.models import Chicken, Hatch, LiveStock


class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = ["dob", "dod", "sex"]


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ["band_color", "band_number", "breed",]


class HatchForm(forms.ModelForm):
    class Meta:
        model = Hatch
        fields = ["start_date", "first_hatch_date", "end_date", "breed", "eggs_started", "eggs_hatched", "equipment", "notes", "complete"]