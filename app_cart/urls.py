from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

# Main Urls
app_name = 'cart'

urlpatterns = [
    path('', login_required(myCart.as_view()), name='myCart'),
    ########## ajax ##########
    path('add', addToCart.as_view(), name='add'),
    path('removeFromCart/<int:pk>/', removeFromCart, name="removeFromCart"),
    path('qtyupdate', qtyUpdate.as_view(), name="qtyUpdate"),
]
