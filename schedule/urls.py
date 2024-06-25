#schedule\urls.py
from django.urls import path

from schedule import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:sch_id>", views.sch, name="day"),
    path("<int:sch_id>/add", views.add, name="add")
]