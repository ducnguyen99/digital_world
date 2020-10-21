from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .utils import *
from .decorators import *

# Create your views here.

def product(request):
    products = Product.objects.all()
    user = request.user

    data = cart_data(request)
    total_item = data['total_item']

    context = {
        'products': products,
        'user': user,
        'total_item': total_item
    }

    response = render(request, 'product.html', context)
    if user.is_authenticated:
        response.delete_cookie('cart')
    return response

def cart(request):
    data = cart_data(request)
    ordered_products = data['ordered_products']
    total_item = data['total_item']
    total_item_price = data['total_item_price']

    context = {
        'ordered_products': ordered_products,
        'total_item': total_item,
        'total_item_price': total_item_price
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
def checkout(request):
    user = request.user
    if user.is_authenticated:
        customer = user.customer 
        order, _ = Order.objects.get_or_create(customer_name=customer, status='Pending')
        ordered_products = order.orderedproduct_set.all()
        total_item = order.get_total_item

    context = {
        'order': order,
        'ordered_products': ordered_products,
        'total_item': total_item
    }

    response = render(request, 'checkout.html', context)
    if user.is_authenticated:
        response.delete_cookie('cart')
    return response

def update_cart(request):
    data = json.loads(request.body)
    customer = request.user.customer
    product_id = data['productId']
    action = data['action']
    product = Product.objects.get(id=product_id)
    order, _ = Order.objects.get_or_create(customer_name=customer, status='Pending')
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

    order, _ = Order.objects.get_or_create(customer_name=customer, status='Pending')

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

def process_order(request):
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, _ = Order.objects.get_or_create(customer_name=customer, status='Pending') 
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        postcode=data['shipping']['zipcode'], )

        order.status = 'Complete'
        order.save()


    return JsonResponse('Payment submitted...', safe=False)


# def create_guest_cart(request):

#     data = cart_data(request)
#     ordered_products = data['ordered_products']
#     try:
#         cart = json.loads(request.COOKIES['cart'])
#     except:
#         cart = {}
#     print('in create')
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer_name=customer, status='Pending')
#     if created:
#         for id in cart:
#             product = Product.objects.get(id=id)
#             OrderedProduct.objects.create(order=order, product=product)
#     else: 
#         order.delete()
#         order = Order.objects.create(customer_name=customer, status='Pending')
#         for id in cart:
#             product = Product.objects.get(id=id)
#             OrderedProduct.objects.create(order=order, product=product, quantity=cart[id]['quantity']) 
#     return None