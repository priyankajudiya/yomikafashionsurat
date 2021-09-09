from django.contrib import admin
from .models import order
# Register your models here.


@admin.register(order)
class orderAdminModel(admin.ModelAdmin):
    list_display = ['user', 'product_sku', 'orderId', 'status']
    list_display_links = ["user", "product_sku"]
