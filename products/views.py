from django.shortcuts import render
from .models import *
# Create your views here.


def product(request):
    products = Product.objects.all()
    customer = Customer.objects.all()
    print(customer)
    for i in customer:
        print(i.user)
    user = request.user
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