from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('stock',)
    ordering = ('-price',)
    list_per_page = 10  # Number of products per page in the admin list view
# Register your models here.
