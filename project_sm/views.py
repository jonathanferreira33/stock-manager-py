from rest_framework import viewsets
from project_sm.models import Product
from project_sm.serializer import ProductSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
