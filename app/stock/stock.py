from django.shortcuts import render

from stock.models import Stock


def index(request):

    context = {
        'stock': Stock.objects.all()
    }

    return render(
        request,
        template_name="stock/stock_index.html",
        context=context
    )
