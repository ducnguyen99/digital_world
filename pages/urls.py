from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('', contact, name='contact'),
    path('', about, name='about'),
]

