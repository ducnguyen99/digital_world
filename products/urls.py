from django.urls import path
from .views import *

urlpatterns = [
    path('product/', product, name='product'),

    path('cart/', cart, name='cart'),
    path('login/', login, name='login')

]