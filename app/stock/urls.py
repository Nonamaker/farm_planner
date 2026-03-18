from django.urls import path

from . import chickens, eggs, hatch, stock

app_name = "stock"

urlpatterns = [
    path("", stock.index, name="stock_index"),

    path("chickens/", chickens.index, name="chickens_index"),
    path("chickens/form/", chickens.update_or_create, name="chickens_create_form"),
    path("chickens/form/<int:pk>/", chickens.update_or_create, name="chickens_update_form"),
    path("chickens/view/<int:pk>/", chickens.view, name="chickens_view"),
    path("chickens/delete/<int:pk>/", chickens.delete, name="chickens_delete"),

    path("egg/", eggs.index, name="egg_index"),
    path("egg/form/", eggs.create, name="egg_day_form"),
    path("egg/form/<int:pk>/", eggs.update, name="egg_update_form"),
    path("egg/view/<int:pk>", eggs.view, name="egg_view"),
    path("egg/delete/<int:pk>", eggs.delete, name="egg_delete"),

    path("hatch/", hatch.index, name="hatch_index"),
    path("hatch/form/", hatch.update_or_create, name="hatch_create_form"),
    path("hatch/form/<int:pk>/", hatch.update_or_create, name="hatch_update_form"),
    path("hatch/view/<int:pk>/", hatch.view, name="hatch_view"),
    path("hatch/delete/<int:pk>/", hatch.delete, name="hatch_delete"),
]