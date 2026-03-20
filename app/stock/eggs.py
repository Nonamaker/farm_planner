""" Contains routes related to the creation, modification, and viewing of the number of eggs
produced per day. """

import datetime as dt
import pandas as pd

import plotly.express as px

from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from stock.models import Chicken, Egg, Stock
from stock.forms import EggForm, EggDayForm


def index(request):

    records = Egg.objects.all()

    data_as_dict = {}
    annotated_records = set(records.values_list("lay_date").annotate(daily_total=Count('id')).order_by("-lay_date"))
    
    for dt_date, daily_total in annotated_records:
        date = dt_date.strftime("%Y-%m-%d")
        if data_as_dict.get(date) is None:
            data_as_dict[date] = {
                'date': date,
                'percent_yield': (daily_total/Chicken.laying_hens_on_date(dt_date))*100
            }

    sorted_data = sorted(data_as_dict.items(), key = lambda k_v: dt.datetime.strptime(k_v[1]['date'], "%Y-%m-%d"))
    data = [x[1] for x in sorted_data]

    df = pd.DataFrame(data=data)

    fig = px.line(
        df,
        x="date",
        y="percent_yield"
    )

    context = {
        'records': records,
        'data': fig.to_json(),
        'json_file': fig.to_json(),
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
