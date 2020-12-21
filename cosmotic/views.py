from django.shortcuts import render
# Create your views here.

from .models import *


def home(request):

    return render(request, 'cosmotic/base.html')


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'cosmotic/products.html', context)