from django.shortcuts import render
from core.models import Currency, Payments, Product, CurrencyHistory
from core.serializers import CurrencyHistorySerializer, ProductSerializer, PaymentSerializer, CurrencySerializer
from rest_framework import views
from rest_framework.response import Response
from django.db.models import Q
from functools import reduce
import operator

# Create your views here.
def index(request):
    context = {"available_tables": ["product", "payment", "currency"]}
    return render(request, 'pages/index.html', context)


def BTCHistory(request):
    return render(request, 'pages/btc-history.html')

class BTCHistoryView(views.APIView):
    def get(self, request):
        data = CurrencyHistory.objects.all()
        data = CurrencyHistorySerializer(data, many=True).data
        response = {}
        response['target_currency'] = None if len(data) == 0 else data[0]['target_currency']
        response['coin'] = None if len(data) == 0 else data[0]['coin']
        response['dates'] = [item['date'] for item in data]
        response['rates'] = [item['rate'] for item in data]
        return Response(response)




class TableView(views.APIView):
    def get(self, request):
        table_name = request.query_params.get("table", "product")
        page = int(request.query_params.get("page", 0))
        query = request.query_params.get("query", None)
        limit = 5
        response = {}
        model, serializer, search_fields = return_model_serializer_by_name_and_search_fields(table_name)
        if model and serializer:
            if query:
                all_data = []
                queries = []
                for field in search_fields:
                    queries.append(Q(**{field + "__icontains": query}))
                all_data = model.objects.filter(reduce(operator.or_, queries))
            else:
                all_data = model.objects.all()

            data = serializer(all_data[page*limit:(page*limit)+limit], many=True).data
        else:
            return Response({"error": "No table was found with this name"}, status=404)

        response = {"data": data, "total_pages": len(all_data) / limit}
        return Response(response)

    def delete(self, request):
        table_name = request.query_params.get("table", None)
        id = request.query_params.get("id", None)
        
        if table_name is None or id is None:
            return Response({"error": "Please provide a table name and an id"}, status=404)
        try:
            if table_name == "product":
                Product.objects.get(id=id).delete()
            elif table_name == "payment":
                Payments.objects.get(id=id).delete()
            elif table_name == "currency":
                Currency.objects.get(id=id).delete()
            else:
                return Response({"error": "No table was found with this name"}, status=404)
        except:
            return Response({"error": "Item was not found"}, status=404)
        return Response({"message": "Deleted Successfully"})

    def put(self, request):
        id = request.data['id']
        table_name = request.query_params.get("table", None)
        try:
            if table_name == "product":
                Product.objects.filter(id=id).update(**request.data)
            elif table_name == "payment":
                Payments.objects.filter(id=id).update(**request.data)
            elif table_name == "currency":
                Currency.objects.filter(id=id).update(**request.data)
            else:
                return Response({"error": "No table was found with this name"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
        return Response({"message": "Put request"})





def return_model_serializer_by_name_and_search_fields(table_name):
    if table_name == "product":
        return Product, ProductSerializer, ("name", "color", "category", "price")
    elif table_name == "payment":
        return Payments, PaymentSerializer, ("name", "email", "card_number", "expiration_date", "cvv", "amount")
    elif table_name == "currency":
        return Currency, CurrencySerializer, ("name", "value_per_bitcoin")
    else:
        return None, None
