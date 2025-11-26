from django.urls import path

from . import beds

app_name = "plots"

urlpatterns = [
    path("beds/", beds.index, name="beds_index"),
    path("beds/form/", beds.update_or_create, name="beds_create_form"),
    path("beds/form/<int:pk>/", beds.update_or_create, name="beds_update_form"),
    path("beds/view/<int:pk>/", beds.view, name="beds_view"),
    path("beds/delete/<int:pk>/", beds.delete, name="beds_delete"),
]