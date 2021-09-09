from app_products.models import product
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from app_cart.models import Cart
from .models import order
import datetime

# Create your views here.

class checkOut(View):
    def get(self, request):
        
        return redirect('cart:myCart')

    def post(self, request):
        orderBy = get_object_or_404(User, username = request.user)
        cartProducts = Cart.objects.filter(user = request.user)
        d=datetime.datetime.now()
        orderid = str(len(cartProducts))+'-'+str(request.user.pk)+str(datetime.datetime.now().strftime("%Y%m%d"))+str(d.timestamp())[11:]
        if not cartProducts:
            return HttpResponse('No products in cart')

        for productObj in cartProducts:
            order.objects.create(
                user = productObj.user,
                orderId = orderid,
                address = f'{orderBy.profile.address}, {orderBy.profile.state}, {orderBy.profile.city}-{orderBy.profile.pincode}',
                product_sku = get_object_or_404(product, pk = str(productObj.product_id)),
                qty = str(productObj.product_qty),
                size = str(productObj.product_size),
                color = str(productObj.product_color),
                status = 'pending'
            ).save()
            productObj.delete()
        
        return HttpResponse('order confirmed')
