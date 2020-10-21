from django.http import HttpResponse
from django.shortcuts import redirect
from .utils import *
from .models import *
from django.http import HttpResponse, HttpResponseRedirect

def create_guest_cart(view_func):
    def wrapper_func(request, *args, **kwargs):
        data = cart_data(request)
        ordered_products = data['ordered_products']
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer_name=customer, status='Pending')
        if created:
            for id in cart:
                product = Product.objects.get(id=id)
                OrderedProduct.objects.create(order=order, product=product)
        else: 
            order.delete()
            order = Order.objects.create(customer_name=customer, status='Pending')
            for id in cart:
                product = Product.objects.get(id=id)
                OrderedProduct.objects.create(order=order, product=product, quantity=cart[id]['quantity']) 
        return view_func(request, *args, **kwargs)
    return wrapper_func

