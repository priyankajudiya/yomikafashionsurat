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
    # queryset = models.product.objects.all().order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super(shop, self).get_context_data(**kwargs)
        context['categorys'] = models.category.objects.all()
        return context
        
    def get_queryset(self):
        queryset = models.product.objects.all().order_by('-upload_date')       
        return queryset
    

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
        all_products = models.product.objects.all().order_by('-upload_date')
        page = request.GET.get('page', 1)
        search = request.GET.get('search')
        catBy = request.GET.get('cat')
        sortBy = request.GET.get('sb')
        priceBy = request.GET.get('pb')
        colorBy = request.GET.get('cb')
        # print(colorBy)


        if search or colorBy:
            from simple_search import search_filter
            search_fields = ['title',]
            query = search
            try:
                results = all_products.filter(search_filter(search_fields, query))
            except:
                results = all_products.filter(search_filter(search_fields, colorBy))


            all_products = results
            
        if catBy:
            all_products = all_products.filter(cat__productCategory=catBy)
        if sortBy == 'lowHigh':
            all_products = all_products.order_by('price')
        if sortBy == 'highLow':
            all_products = all_products.order_by('-price')
        if priceBy:
            try:
                minPrice = priceBy.split('-')[0]
                maxPrice = priceBy.split('-')[1]
                all_products = all_products.filter(price__gte = minPrice,price__lte=maxPrice)
            except:
                all_products = all_products.filter(price__gte = 5000)

        
        paginator = Paginator(all_products, 3)
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        ######## Context ########
        context['categorys'] = models.category.objects.all()
        context['products'] = product
        context['categoryName'] = catBy     

        return render(request, 'app_products/shop-filter.html', context)
