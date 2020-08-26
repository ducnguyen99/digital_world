from django.db import models

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
    image = models.ImageField(null = True, blank = True, upload_to='static/media')
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    username = models.CharField(max_length = 120) 
    name = models.CharField(max_length = 120)
    email = models.EmailField(max_length = 120)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Complete', 'Complete'),
    ] 
    DELIVERY_OPTION = [
        ('Pickup', 'Pickup'),
        ('Delivery', 'Delivery'),
    ]
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True) # should be set null = False
    date_ordered = models.DateField(auto_now_add=True)
    delivery_option = models.CharField(max_length= 120, choices=DELIVERY_OPTION)  
    status = models.CharField(max_length= 120, choices=STATUS_CHOICES) 

    def __str__(self):
        return self.id
    
class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default = 0)
    def __str__(self):
        return self.product

    def __unicode__(self):
        return self.product 

class ShippingAddress(models.Model):
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    postcode = models.CharField(max_length=120)

    def __str__(self):
        return self.address

    