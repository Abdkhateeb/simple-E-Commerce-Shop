from django.shortcuts import render
from rest_framework import generics

from .models import Product
from .Serializers import ProductSerializer  



class ProductListApi(generics.ListAPIView):
    """
    API view to retrieve list of products or create a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    
    
class ProductCreateApi(generics.CreateAPIView):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    
    
class ProductDetailApi(generics.RetrieveAPIView):
    """
    API view to retrieve a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     
    
class ProductDeleteApi(generics.DestroyAPIView):
    """
    API view to delete a product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    