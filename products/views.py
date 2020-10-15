from django.shortcuts import render
from .models import *

# Create your views here.


def product(request):
    products = Product.objects.all()
    customer = Customer.objects.all()
    user = request.user
    print(user.is_authenticated)
    print(type(user))
    context = {
        'products': products,
        'user': user
    }
    return render(request, 'product.html', context)

def cart(request):
    context = {}
    return render(request, 'cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)