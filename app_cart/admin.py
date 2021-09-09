from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ('pk','user', 'product_id', 'product_qty', 'product_size', 'product_color')
