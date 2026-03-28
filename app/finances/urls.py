from django.urls import path

from . import finances, transactions

app_name = "finances"

urlpatterns = [
    path("", finances.index, name="finances_index"),

    path("sales/form/", transactions.update_or_create, name="sales_create_form"),
    path("sales/form/<int:pk>", transactions.update_or_create, name="sales_update_form"),
    path("sales/view/<int:pk>", transactions.view, name="sales_view"),
    path("saltes/delete/<int:pk>", transactions.delete, name="sales_delete"),
]