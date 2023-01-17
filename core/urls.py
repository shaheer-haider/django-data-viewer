from django.contrib import admin
from django.urls import path
from core import views
from core.views import TableView, BTCHistory, BTCHistoryView, dynamic_table, DynamicJSONData

urlpatterns = [
    path("", views.index, name="index"),
    path("table-view/", TableView.as_view(), name="Table View"),
    path("graph/", BTCHistory, name="BTC History"),
    path("btc-history/", BTCHistoryView.as_view(), name="BTC History API"),
    path("dynamic-table/", dynamic_table, name="dynamic table"),
    path("dynamic-json/", DynamicJSONData.as_view(), name="dynamic json"),
]
