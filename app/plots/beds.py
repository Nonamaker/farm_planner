from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from plots.models import Bed
from plots.forms import BedForm


def index(request):
    return HttpResponse("Index")

def update_or_create(request, pk=None):
    if pk is None:
        bed = Bed()
    else:
        bed = get_object_or_404(Bed, pk=pk)
    del pk
    
    if request.method == "POST":
        form = BedForm(request.POST)
        if form.is_valid():
            bed.name = form.cleaned_data['name']
            bed.width = 1
            bed.length = 1
            bed.save()
            return HttpResponseRedirect(
                reverse(
                    'plots:beds_view',
                    kwargs={'pk': bed.pk}
                )
            )
    else:
        if bed.pk:
            form = BedForm(instance=bed)
        else:
            form = BedForm()

    context = {
        'form': form
    }

    return render(
        request,
        template_name="plots/bed_form.html",
        context=context
    )


def view(request, pk):
    bed = get_object_or_404(Bed, pk=pk)
    return render(
        request,
        template_name="plots/bed_view.html",
        context={'bed': bed}
    )

def delete(request, pk):
    return HttpResponse("Delete")
