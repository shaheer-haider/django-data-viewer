from django.shortcuts import render
from core.models import Currency, Payments, Product
from core.serializers import ProductSerializer, PaymentSerializer, CurrencySerializer
from rest_framework import request, views, response
from rest_framework.response import Response
import math

# Create your views here.
def index(request):
    context = {"available_tables": ["product", "payment", "currency"]} 
    return render(request, 'pages/index.html', context)


class TableView(views.APIView):
    def get(self, request):
        table_name = request.query_params.get("table", "product")
        page = int(request.query_params.get("page", 0))
        limit = 5
        response = {}
        if table_name == "product":
            all_data = Product.objects.all()
            data = ProductSerializer(all_data[page*limit:(page*limit)+limit], many=True).data
        elif table_name == "payment":
            all_data = Payments.objects.all()
            data = PaymentSerializer(all_data[page*limit:(page*limit)+limit], many=True).data  
        elif table_name == "currency":
            all_data = Currency.objects.all()
            data = CurrencySerializer(all_data[page*limit:(page*limit)+limit], many=True).data
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


