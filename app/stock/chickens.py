from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from stock.models import Chicken, LiveStock, Stock
from stock.forms import ChickenForm, LiveStockForm


def index(request):
    return HttpResponse("Index")

def update_or_create(request, pk=None):
    if pk is None:
        chicken = Chicken()
        livestock = LiveStock()
        stock = Stock()
    else:
        chicken = get_object_or_404(Chicken, pk=pk)
        livestock = chicken.livestock
        stock = livestock.stock
    del pk
    
    if request.method == "POST":
        chicken_form = ChickenForm(request.POST)
        livestock_form = LiveStockForm(request.POST)
        if chicken_form.is_valid() and livestock_form.is_valid():
            stock.save()

            livestock.stock = stock
            livestock.dob = livestock_form.cleaned_data['dob']
            livestock.dod = livestock_form.cleaned_data['dod']
            livestock.sex = livestock_form.cleaned_data['sex']
            livestock.save()

            chicken.livestock = livestock
            chicken.band_color = chicken_form.cleaned_data['band_color']
            chicken.band_number = chicken_form.cleaned_data['band_number']
            chicken.breed = chicken_form.cleaned_data['breed']
            chicken.save()
            return HttpResponseRedirect(
                reverse(
                    'stock:chickens_view',
                    kwargs={'pk': chicken.pk}
                )
            )
    else:
        if chicken.pk:
            livestock_form = LiveStockForm(instance=livestock)
            chicken_form = ChickenForm(instance=chicken)
        else:
            livestock_form = LiveStockForm()
            chicken_form = ChickenForm()

    context = {
        'chicken_form': chicken_form,
        'livestock_form': livestock_form
    }

    return render(
        request,
        template_name="stock/chickens_form.html",
        context=context
    )


def view(request, pk):
    chicken = get_object_or_404(Chicken, pk=pk)
    return render(
        request,
        template_name="stock/chickens_view.html",
        context={'chicken': chicken}
    )

def delete(request, pk):
    return HttpResponse("Delete")
