""" Contains routes related to the creation, modification, and viewing of the number of eggs
produced per day. """

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from finances.models import Transaction
from finances.forms import TransactionForm


def update_or_create(request, pk=None):
    if pk is None:
        transaction = Transaction()
    else:
        transaction = get_object_or_404(Transaction, pk=pk)
    del pk
    
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction.value = transaction_form.cleaned_data['value']
            transaction.date = transaction_form.cleaned_data['date']
            transaction.category = transaction_form.cleaned_data['category']
            transaction.save()
            return HttpResponseRedirect(
                reverse(
                    'stock:transactions_view',
                    kwargs={'pk': transaction.pk}
                )
            )
    else:
        if transaction.pk:
            transaction_form = TransactionForm(instance=transaction)
        else:
            transaction_form = TransactionForm()

    context = {
        'form': transaction_form
    }

    return render(
        request,
        template_name="finances/transactions/form.html",
        context=context
    )


def view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(
        request,
        template_name="finances/transactions/view.html",
        context={'transaction': transaction}
    )

def delete(request, pk):
    return HttpResponse("Delete")
