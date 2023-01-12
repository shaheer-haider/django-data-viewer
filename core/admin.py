from django.contrib import admin

from core.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "color", "category", "price")

# Register your models here.
admin.site.register(Product, ProductAdmin)