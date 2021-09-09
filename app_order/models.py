from django.db import models
from django.contrib.auth.models import User
from app_products.models import product
from django.utils import timezone

# Create your models here.

class order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("shiped", "Shiped"),
        ("delivered", "Delivered"),
        ("cancel", "Cancel"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderCreatedDate = models.DateTimeField(default=timezone.now)
    orderId = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=1000)
    product_sku = models.ForeignKey(product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
