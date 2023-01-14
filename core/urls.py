from django.contrib import admin
from django.urls import path
from core import views
from core.views import TableView, BTCHistory, BTCHistoryView

urlpatterns = [
    path("", views.index, name="index"),
    path("table-view/", TableView.as_view(), name="Table View"),
    path("graph/", BTCHistory, name="BTC History"),
    path("btc-history/", BTCHistoryView.as_view(), name="BTC History API"),
]
