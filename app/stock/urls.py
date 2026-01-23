from django.urls import path

from . import chickens, stock

app_name = "stock"

urlpatterns = [
    path("", stock.index, name="stock_index"),
    path("chickens/form/", chickens.update_or_create, name="chickens_create_form"),
    path("chickens/form/<int:pk>/", chickens.update_or_create, name="chickens_update_form"),
    path("chickens/view/<int:pk>/", chickens.view, name="chickens_view"),
    path("chickens/delete/<int:pk>/", chickens.delete, name="chickens_delete"),
]