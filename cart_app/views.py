from django.shortcuts import render, redirect
from .models import Cart
from merchandise.models import Product
from orders.models import Order
# Create your views here.

def get_or_create_cart(request):
    global my_cart
    global new_cart
    cart_pk = request.session.get('cart_pk',None)
    user = request.user
    if cart_pk is None:
        new_cart = True
        if user.is_anonymous:
            my_cart = Cart.objects.create(user=None)
        elif user.is_authenticated:
            my_cart = Cart.objects.create(user=user)
        request.session['cart_pk'] = my_cart.pk
    else:
        new_cart = False
        my_cart = Cart.objects.filter(pk=cart_pk).first()
        if user.is_authenticated and my_cart.user is None:
            my_cart.user = request.user
            my_cart.save()
    return new_cart,my_cart

def cart_index(request):
    new_cart, my_cart = get_or_create_cart(request)
    request.session['item_count'] = my_cart.products.count()
    return render(request,'cart_app/cart_main.html',{'my_cart':my_cart})

def cart_add(request):
    productId = request.POST.get('productId')
    new_cart, my_cart = get_or_create_cart(request)
    if productId:
        try:
            product = Product.objects.get(id=productId)
        except Product.DoesNotExist:
            return redirect('cart_app:cart')
        my_cart.products.add(product)
    return redirect('cart_app:cart')

def cart_remove(request):
    productId = request.POST.get('productId')
    new_cart, my_cart = get_or_create_cart(request)
    product = Product.objects.get(id=productId)
    my_cart.products.remove(product)
    return redirect('cart_app:cart')

def checkout_page(request):
    new_cart, my_cart = get_or_create_cart(request)
    if not new_cart:
        my_order = Order.objects.filter(cart=my_cart).first()
    elif my_cart.products.count()==0:
        return redirect('cart_app:cart')
    return render(request,'cart_app/checkout_page.html',{'my_order':my_order})