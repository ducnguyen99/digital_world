import json
from .models import *

def get_cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    ordered_products = []
    total_item = 0
    total_item_price = 0
    for id in cart:
        product = Product.objects.get(id=id)
        total = (product.price * cart[id]['quantity'])
        total_item += cart[id]['quantity']
        total_item_price += (product.price * cart[id]['quantity'])

        ordered_product = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'imgURL': product.imgURL,
            },
            'quantity': cart[id]['quantity'],
            'total': total,
        }
        ordered_products.append(ordered_product)
    return {'ordered_products':ordered_products, 'total_item': total_item, 'total_item_price': total_item_price}

def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer_name=customer, status='Pending')
        ordered_products = order.orderedproduct_set.all()
        total_item = order.get_total_item
        total_item_price = order.get_total_item_price
    else:
        cookie_data = get_cookie_cart(request)
        ordered_products = cookie_data['ordered_products']
        total_item = cookie_data['total_item']
        total_item_price = cookie_data['total_item_price']


    return {'total_item': total_item, 'total_item_price': total_item_price, 'ordered_products': ordered_products}


