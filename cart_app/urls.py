from django.urls import path
from . import views

app_name='cart_app'

urlpatterns = [
    path('cart/',views.cart_index,name='cart'),
    path('add/',views.cart_add,name='add_product'),
    path('remove/',views.cart_remove,name='remove_product')
]