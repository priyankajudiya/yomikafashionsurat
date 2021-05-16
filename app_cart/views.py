from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, CreateView

# import Model 
from .models import Cart
from app_products.models import product

# Create your views here.

class myCart(View):
    def get(self, request):
        try: context = {'cart': Cart.objects.filter(user=request.user)}
        except: context = {}
        return render(request, 'app_cart/myCart.html', context)

################# Product add to cart Ajax
class addToCart(View):
    def post(self, request):
        if request.is_ajax():
            produc, created = Cart.objects.get_or_create(
                                    user = request.user,
                                    product_id = product.objects.get(pk=int(request.POST.get('product_id'))),
                                    product_size = request.POST.get('product_size'),
                                    product_color = request.POST.get('product_color'),
                                )
            qty = produc.product_qty = request.POST.get('product_qty')
            produc.save()
            try:# if created than update
                if not created:
                    return JsonResponse({'type':'update','msg':'Cart Updated', 'qty':qty})
                else:
                    return JsonResponse({'type':'create','msg': 'Product Added To Cart', 'qty': qty})

            except Exception as e:
                return HttpResponse(f'Magic Happen!: {e}')
            

################################### product delete from cart
def removeFromCart(request, pk):
    obj = get_object_or_404(Cart, id=pk)
    if request.user.is_authenticated and request.user.pk == obj.user.pk:
        obj.delete()
                
    return redirect(request.GET.get('next'))
