from django import forms

from finances.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["value", "date"]
        labels = {
            'value': "Value",
            'date': "Date",
            'category': "Category"
        }
        widgets = {
            'category': forms.Textarea(attrs={'rows': 1})
        }

