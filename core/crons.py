import requests
from core.models import Currency

def update_currencies():
    currencies_data = requests.get("https://blockchain.info/ticker").json()
    for currency, data in currencies_data.items():
        try:
            currency = Currency.objects.get(name=currency)
            currency.value_per_bitcoin=data["last"]
            currency.save()
        except Currency.DoesNotExist:
            Currency.objects.create(name=currency, value_per_bitcoin=data["last"])
