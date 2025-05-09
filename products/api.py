from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .Serializers import ProductSerializer  



class ProductListApi(generics.ListCreateAPIView):
    """
    API view to retrieve list of products or create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    