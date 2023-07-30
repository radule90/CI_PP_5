from django.shortcuts import render, redirect
from .models import Cart, CartItem
from product.models import Product

# Create your views here.

def _cart_id(request):
    '''
    Function to get the current session cart ID.
    '''
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add(request, product_id):
    '''
    Function based view to add product in cart
    Creates new cart if does not exist
    Increments quantity
    '''
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    print(cart_item)
    return redirect('cart')


def cart(request):
    context = {}
    template = 'cart/cart.html'
    return render(request, template, context)
