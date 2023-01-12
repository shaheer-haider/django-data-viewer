from django.contrib import admin

from core.models import Product, Payments, Currency

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "category", "price")

# Register your models here.
admin.site.register(Product, ProductAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "card_number", "expiration_date", "cvv", "amount")
    
admin.site.register(Payments, PaymentsAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "value_per_bitcoin")
    
admin.site.register(Currency, CurrencyAdmin)