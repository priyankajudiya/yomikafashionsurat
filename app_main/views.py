from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View

from app_products.models import product
import random
# Create your views here.

class index(View):
    def get(self, request):
        # products = product.objects.all().order_by('-id')
        items = list(product.objects.all())
        random.shuffle(items)

        context = {
            'products': items[:5]
        }
        return render(request, 'app_main/index.html', context)

class about(View):
    def get(self, request):
        return render(request, 'app_main/about.html')


class contact(View):
    def get(self, request):
        return render(request, 'app_main/contact.html')