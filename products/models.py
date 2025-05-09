from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=300)
    product_description = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name

