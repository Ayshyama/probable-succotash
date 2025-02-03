from django.urls import path
from .views import order_form, order_success, get_products

urlpatterns = [
    path('form/', order_form, name='order_form'),
    path('success/', order_success, name='order_success'),
    path('api/products/', get_products, name='get_products'),
]
