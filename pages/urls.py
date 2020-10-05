from django.urls import path
from .views import *

urlpatterns = [
    path('/home', home, name='home'),
    path('/contact', contact, name='contact'),
    path('', about, name='about'),
]

