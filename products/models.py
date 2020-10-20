from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer
# Create your models here.

class Product(models.Model):
    CATEGORY = [
        ('PS4', 'PS4'),
        ('Nitendo Switch', 'Nitendo Switch'),
        ('PC Gaming', 'PC Gaming')
    ]
    name = models.CharField(max_length = 120)
    price = models.DecimalField(max_digits = 7, decimal_places=2 )
    category = models.CharField(max_length=120, choices=CATEGORY, null=True)
    image = models.ImageField(null = True, blank = True)
    
    def __str__(self):
        return str(self.name)
    
    @property
    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    ] 
    DELIVERY_OPTION = [
        ('Pickup', 'Pickup'),
        ('Standard Delivery', 'Standard Delivery'),
        ('Express Delivery', 'Express Delivery'),
    ]

    PRICE_OPTION = [
        (0.00, 0.00),
        (5.00, 5.00),
        (12.00, 12.00),
    ]
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True) # should be set null = False
    date_ordered = models.DateField(auto_now_add=True)
    delivery_option = models.CharField( max_length= 120, choices=DELIVERY_OPTION, default='Pickup')  
    status = models.CharField(max_length= 120, choices=STATUS_CHOICES, default='Pending') 
    delivery_price = models.DecimalField(blank=True, null=True, max_digits = 7, decimal_places=2, choices= PRICE_OPTION, default=0.00)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_item_price(self):
        ordered_product = self.orderedproduct_set.all()
        total = sum([item.total for item in ordered_product])
        return total

    @property
    def get_total_order_price(self):
        total = self.get_total_item_price + self.delivery_price
        return total

    @property
    def get_total_item(self):
        ordered_product = self.orderedproduct_set.all()
        total = sum([item.quantity for item in ordered_product])
        return total

class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.product)

    def __unicode__(self):
        return self.product 
    

    @property
    def total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postcode = models.CharField(max_length=120)

    def __str__(self):
        return self.address

    