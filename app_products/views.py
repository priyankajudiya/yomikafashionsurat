from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View, DetailView, ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import models
from app_cart.models import Cart

from random import shuffle
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

class shop(ListView):
    model = models.product
    template_name = 'app_products/shop.html'
    context_object_name = "products"
    paginate_by = 4
    queryset = models.product.objects.all().order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super(shop, self).get_context_data(**kwargs)
        context['categorys'] = models.category.objects.all()
        return context

################################### product Details view


class productDetails(DetailView):
    model = models.product
    template_name = 'app_products/product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(productDetails, self).get_context_data(**kwargs)

        relatedProducts = list(models.product.objects.filter(cat__productCategory = self.object.cat).exclude(id=self.object.id))
        shuffle(relatedProducts)
        
        ######## Context ########
        context['relatedProducts'] = relatedProducts[:2]
        return context

################################### Product filter
class productFilter(View):
    def get(self, request):
        context = {}
        search = request.GET.get('filter')
        products = models.product.objects.filter(cat__productCategory=search)

        page = request.GET.get('page', 1)

        paginator = Paginator(products, 3)
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        ######## Context ########
        context['categorys'] = models.category.objects.all()
        context['products'] = product
        context['categoryName'] = search
        

        return render(request, 'app_products/shop-filter.html', context)
