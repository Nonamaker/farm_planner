from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from stock.models import Hatch
from stock.forms import HatchForm


def index(request):
    return HttpResponse("Index")

def update_or_create(request, pk=None):

    # TODO Prohibit modification if record is complete.

    if pk is None:
        hatch = Hatch()
    else:
        hatch = get_object_or_404(Hatch, pk=pk)
    del pk
    
    if request.method == "POST":
        hatch_form = HatchForm(request.POST)
        if hatch_form.is_valid():
            hatch.start_date = hatch_form.cleaned_data['start_date']
            hatch.end_date = hatch_form.cleaned_data['end_date']
            hatch.first_hatch_date = hatch_form.cleaned_data['first_hatch_date']
            hatch.eggs_started = hatch_form.cleaned_data['eggs_started']
            hatch.eggs_hatched = hatch_form.cleaned_data['eggs_hatched']
            hatch.breed = hatch_form.cleaned_data['breed']
            hatch.equipment = hatch_form.cleaned_data['equipment']
            hatch.notes = hatch_form.cleaned_data['notes']

            prior_state = hatch.complete
            hatch.complete = hatch_form.cleaned_data['complete']

            if hatch.complete is True and prior_state is False:
                hatch.create_chickens()

            hatch.save()
            return HttpResponseRedirect(
                reverse(
                    'stock:hatch_view',
                    kwargs={'pk': hatch.pk}
                )
            )
    else:
        if hatch.pk:
            hatch_form = HatchForm(instance=hatch)
        else:
            hatch_form = HatchForm()

    context = {
        'hatch_form': hatch_form,
    }

    return render(
        request,
        template_name="stock/hatch_form.html",
        context=context
    )


def view(request, pk):
    hatch = get_object_or_404(Hatch, pk=pk)
    return render(
        request,
        template_name="stock/hatch_view.html",
        context={'hatch': hatch}
    )

def delete(request, pk):
    return HttpResponse("Delete")
