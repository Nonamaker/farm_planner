from django import forms

from plots.models import Bed

class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields = ["name"]