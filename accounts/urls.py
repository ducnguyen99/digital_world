from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('cartt/', cart, name='caart'),
    path('login/', login, name='login')

]