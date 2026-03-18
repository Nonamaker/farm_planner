""" Contains routes related to the creation, modification, and viewing of the number of eggs
produced per day. """

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from stock.models import Egg, Stock
from stock.forms import EggForm, EggDayForm


def index(request):

    records = Egg.objects.all()

    context = {
        'records': records,
        'title': "Egg Index",
        'sidebar_links_template': "stock/eggs/index_sidebar_links.html"
    }

    return render(
        request,
        template_name="stock/eggs/index.html",
        context=context
    )

def create(request):
    """ Used for bulk-creating Egg records via the EggDayForm. """

    if request.method == "POST":
        form = EggDayForm(request.POST)
        if form.is_valid():
            for _ in range(form.cleaned_data['quantity']):
                stock = Stock.objects.create()
                Egg.objects.create(
                    lay_date=form.cleaned_data['date'],
                    stock=stock
                )
            return HttpResponseRedirect(
                reverse(
                    'stock:egg_index'
                )
            )
    elif request.method == "GET":
        form = EggDayForm()

    context = {
        'form': form
    }

    return render(
        request,
        template_name="stock/eggs/egg_day_form.html",
        context=context
    )

def update(request, pk):
    
    # Modify existing record
    egg = get_object_or_404(Egg, pk=pk)
    stock = egg.stock
    del pk
    
    if request.method == "POST":
        egg_form = EggForm(request.POST)
        if egg_form.is_valid():
            egg.lay_date = egg_form.cleaned_data['lay_date']
            egg.condition = egg_form.cleaned_data['condition']
            egg.stock = stock
            egg.save()
            return HttpResponseRedirect(
                reverse(
                    'stock:eggs_view',
                    kwargs={'pk': egg.pk}
                )
            )
    else:
        if egg.pk:
            egg_form = EggForm(instance=egg)

    context = {
        'egg_form': egg_form
    }

    return render(
        request,
        template_name="stock/eggs/form.html",
        context=context
    )


def view(request, pk):
    egg = get_object_or_404(Egg, pk=pk)
    return render(
        request,
        template_name="stock/eggs/view.html",
        context={'egg': egg}
    )

def delete(request, pk):
    return HttpResponse("Delete")
