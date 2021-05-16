from django.db import models
from django.contrib.auth.models import User
from app_products.models import product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product_id = models.ForeignKey(product, on_delete = models.CASCADE)
    product_color = models.CharField(max_length = 100)
    product_size = models.CharField(max_length = 50)
    product_qty = models.IntegerField(default=1)

    class Meta:
        ordering = ('product_id',)
