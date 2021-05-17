from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View, DetailView
from . import models
from app_cart.models import Cart
# Create your views here.

#################################### all Product Shop
# class shop(View):
#     def get(self, request):
#         categorys = models.category.objects.all()
#         products = models.product.objects.all()
#         context = {
#             'categorys': categorys,
#             'products': products,
#         }
#         return render(request, 'app_products/shop.html', context)

###################################################
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class shop(ListView):
    model = models.product
    template_name = 'app_products/shop.html'
    context_object_name = "products"
    paginate_by = 4
    queryset = models.product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(shop, self).get_context_data(**kwargs)
        context['categorys'] = models.category.objects.all()
        return context

################################### product Details view


class productDetails(DetailView):
    model = models.product
    template_name = 'app_products/product-detail.html'
    context_object_name = 'product'

################################### Product filter
class productFilter(View):
    def get(self, request):
        context = {}
        search = request.GET.get('filter')
        
        products = models.product.objects.filter(cat__productCategory=search)
            
        context['categorys'] = models.category.objects.all()
        context['products'] = products

        return render(request, 'app_products/shop-filter.html', context)
