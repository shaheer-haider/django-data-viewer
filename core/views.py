from django.shortcuts import render
from core.models import Product
from core.serializers import ProductSerializer
from rest_framework import request, views, response
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

class TableView(views.APIView):
    def get(self, request):
        table_name = request.query_params.get("table", "product")
        
        if table_name == "product":
            data = ProductSerializer(
                Product.objects.all(), many=True
                ).data
        else:
            data = {"error": "No table was found with this name"}
        return Response(data)
            
    