from django.contrib import admin
from django.urls import path
from core import views
from core.views import TableView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", views.index, name="index"),
    path("table-view/", TableView.as_view(), name="Table View")
]
