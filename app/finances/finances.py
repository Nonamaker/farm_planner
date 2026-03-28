from django.shortcuts import render

from stock.models import Stock

from finances.models import Transaction


def index(request):

    context = {
        'stock': Transaction.objects.all(),
        'title': "Finances Index",
    }

    return render(
        request,
        template_name="finances/index.html",
        context=context
    )
