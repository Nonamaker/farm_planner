from django import forms

from stock.models import Chicken, Hatch, LiveStock


class LiveStockForm(forms.ModelForm):
    class Meta:
        model = LiveStock
        fields = ["dob", "dod", "sex"]
        labels = {
            'dob': "Date of Birth",
            'dod': "Date of Death",
            'sex': "Sex"
        }
        widgets = {
            'sex': forms.Textarea(attrs={'rows': 1})
        }


class ChickenForm(forms.ModelForm):
    class Meta:
        model = Chicken
        fields = ["band_color", "band_number", "breed"]
        labels = {
            'band_color': "Band Color",
            'band_number': "Band Number",
            'breed': "Breed"
        }
        widgets = {
            'band_color': forms.Textarea(attrs={'rows': 1})
        }


class HatchForm(forms.ModelForm):
    class Meta:
        model = Hatch
        fields = ["start_date", "first_hatch_date", "end_date", "breed", "eggs_started", "eggs_hatched", "equipment", "notes", "complete"]
        labels = {
            'start_date': "Start Date",
            'first_hatch_date': "First Hatch Date",
            'end_date': "End Date",
            'breed': "Breed",
            'eggs_started': "Number of Eggs Started",
            'eggs_hatched': "Number of Eggs Hatched",
            'equipment': "Equipment",
            'notes': "Notes",
            'complete': "Complete?"
        }
        widgets = {
            'equipment': forms.Textarea(attrs={'rows': 1})
        }