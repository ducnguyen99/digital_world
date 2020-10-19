from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('product/', product, name='product'),

    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_cart/', update_cart, name='update_cart'),
    path('update_order_delivery/', update_order_delivery, name='update_order_delivery')

]


# urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)