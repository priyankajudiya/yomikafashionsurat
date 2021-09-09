from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.category)
class categoryAdminModel(admin.ModelAdmin):
    list_display = ('productCategory',)

@admin.register(models.product)
class productAdminModel(admin.ModelAdmin):
    list_display = ('pk','title', 'seller', 'cat', 'price', 'upload_date')
    list_filter = ('cat', 'price')
    # list_per_page = 2
    search_fields = ('title',)
