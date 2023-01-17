from django.contrib import admin

from core.models import CurrencyHistory, DynamicJson, Product, Payments, Currency

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "category", "price")
    search_fields = ("name", "color", "category", "price")
# Register your models here.
admin.site.register(Product, ProductAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "card_number", "expiration_date", "cvv", "amount")
    search_fields = ("name", "email", "card_number", "expiration_date", "cvv", "amount")

admin.site.register(Payments, PaymentsAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "value_per_bitcoin")
    search_fields = ("name", "value_per_bitcoin")
    
admin.site.register(Currency, CurrencyAdmin)

class CurrencyHistoryAdmin(admin.ModelAdmin):
    list_display = ("date", "rate", "coin", "target_currency")
    
admin.site.register(CurrencyHistory, CurrencyHistoryAdmin)

class DynamicJsonAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
admin.site.register(DynamicJson, DynamicJsonAdmin)