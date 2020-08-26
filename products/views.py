from django.shortcuts import render
from .models import *
# Create your views here.


def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    print(products)
    return render(request, 'product.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)