from django.shortcuts import render

from stock.models import Stock


def index(request):

    context = {
        'stock': Stock.objects.all(),
        'title': "Stock Index",
        'sidebar_links_template': "stock/index_sidebar_links.html"
    }

    return render(
        request,
        template_name="stock/index.html",
        context=context
    )
