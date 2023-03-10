from core.models import DynamicJson, Product, Payments, Currency, CurrencyHistory
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
        

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class CurrencyHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyHistory
        fields = "__all__"


class DynamicJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicJson
        fields = "__all__"