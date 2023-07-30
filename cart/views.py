from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
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


def remove(request, product_id):
    '''
    Function based view to decrement quantity of product from the cart.
    '''
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart)
    except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
        raise Http404

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_item(request, product_id):
    '''
    Function based view to handle removing product completely from the cart.
    '''
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart)
    except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
        raise Http404

    cart_item.delete()

    return redirect('cart')


def cart(request):
    '''
    Function based view to display cart with cart items
    '''
    total = 0
    cart_items = None
    quantity = 0
    tax = 0
    price_without_tax = 0
    # Try to get cart object using the cart_id obtained from the session.
    cart_id = _cart_id(request)
    try:
        cart = Cart.objects.get(cart_id=cart_id)
        
        # Filter all active cart items for that cart.
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            # Calculate the total price, tax and product quantity in cart.
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        # Calculate tax and price without tax
        tax = round(((19 * total) / 100), 2)
        price_without_tax = total - tax

    except ObjectDoesNotExist:
        # If doesn't exist send empty context
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'price_without_tax': price_without_tax,
        'active_shop': 'active_shop',
    }
    template = 'cart/cart.html'
    return render(request, template, context)
