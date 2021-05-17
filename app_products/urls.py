from django.urls import path
from . import views
# Main Urls

app_name = 'products'

urlpatterns = [
    path('shop', views.shop.as_view(), name='shop'),
    path('shop/detail/<int:pk>/<str:slug>', views.productDetails.as_view(), name='productDetails'),
    path('shop?', views.productFilter.as_view(), name='productFilter'),
]
