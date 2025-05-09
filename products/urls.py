from django.urls import path
from .api import ProductListApi, ProductCreateApi, ProductDetailApi, ProductDeleteApi
# from .api import ProductListApi, ProductCreateApi, ProductDetailApi, ProductUpdateApi, ProductDeleteApi


urlpatterns = [
    path('products/', ProductListApi.as_view(), name='product-list'),
    path('products/create', ProductCreateApi.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailApi.as_view(), name='product-detail'),
    path('products/delete/<int:pk>/', ProductDeleteApi.as_view(), name='product-delete'),   
    
    # Add other API endpoints here  
]
