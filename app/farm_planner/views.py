from django.shortcuts import render


def index(request):

    context = {
        'title': "Farm Planner",
    }

    return render(
        request,
        template_name="index.html",
        context=context
    )
