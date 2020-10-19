from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.


def product(request):
    products = Product.objects.all()
    user = request.user
    if user.is_authenticated:
        customer = user.customer 
        order, _ = Order.objects.get_or_create(customer_name=customer)
        cart_total = order.get_total_item
    else:
        cart_total = 0 
    context = {
        'products': products,
        'user': user,
        'cart_total': cart_total
    }
    return render(request, 'product.html', context)

def cart(request):
    user = request.user
    if user.is_authenticated:
        customer = user.customer 
        order, _ = Order.objects.get_or_create(customer_name=customer)
        ordered_product = order.orderedproduct_set.all()
        cart_total = order.get_total_item
    else:
        cart_total = 0  
    context = {
        'order': order,
        'ordered_product': ordered_product,
        'cart_total': cart_total
    }
    return render(request, 'cart.html', context)

def checkout(request):
    user = request.user
    if user.is_authenticated:
        customer = user.customer 
        order, _ = Order.objects.get_or_create(customer_name=customer)
        ordered_product = order.orderedproduct_set.all()
        cart_total = order.get_total_item
    else:
        cart_total = 0  
    context = {
        'order': order,
        'ordered_product': ordered_product,
        'cart_total': cart_total
    }
    return render(request, 'checkout.html', context)

def update_cart(request):
    data = json.loads(request.body)
    customer = request.user.customer
    product_id = data['productId']
    action = data['action']
    product = Product.objects.get(id=product_id)
    order, _ = Order.objects.get_or_create(customer_name=customer)
    order_item, _ = OrderedProduct.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = order_item.quantity + 1
    elif action == 'remove':
        order_item.quantity = order_item.quantity - 1
    order_item.save()

    if order_item.quantity <= 0 or action == 'delete':
        order_item.delete()
    return JsonResponse("Item was added", safe=False)

def update_order_delivery(request):
    data = json.loads(request.body)
    customer = request.user.customer
    delivery_option = data['deliveryOption']

    order, _ = Order.objects.get_or_create(customer_name=customer)

    print(data)
    if delivery_option == 'pickup':
        order.delivery_option = 'Pickup'
        order.delivery_price = 0
    elif delivery_option == 'standard':
        order.delivery_option = 'Standard Delivery'
        order.delivery_price = 5
    elif delivery_option == 'express':
        order.delivery_option = 'Express Delivery'
        order.delivery_price = 12
    order.save()
    return JsonResponse("Item was added", safe=False)