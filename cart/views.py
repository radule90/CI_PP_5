from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, CartItem
from product.models import Product, Variation
from django.contrib.auth.decorators import login_required
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
    Increments quantity of products by one
    '''
    current_user = request.user
    product = Product.objects.get(id=product_id)
    # Check if user authenticated
    if current_user.is_authenticated:
        product_variation = []
        if request.method == 'POST':
            # Loop through the POST data to find variations and
            # add them to the 'product variation list'.
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product,
                                                      category__iexact=key,
                                                      value__iexact=value)
                    product_variation.append(variation)
                except Variation.DoesNotExist:
                    pass
        # Check if the product is already in the cart.
        item_already_in_cart = CartItem.objects.filter(
            product=product, user=current_user).exists()
        # If product exists, prepare to update its quantity.
        if item_already_in_cart:
            cart_item = CartItem.objects.filter(
                product=product, user=current_user)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)

            # If this product variation exists in the cart, update its quantity
            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # If variation doesn't exist, create a new cart item.
                item = CartItem.objects.create(
                    product=product, quantity=1, user=current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            # If product doesn't exist in the cart, create a new cart item.
            cart_item = CartItem.objects.create(
                product=product,
                user=current_user,
                quantity=1,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')
    # For non authenticated user
    else:
        product_variation = []
        if request.method == 'POST':
            # Loop through the POST data to find variations and
            # add them to the 'product variation list'.
            for item in request.POST:
                key = item
                value = request.POST[key]
                try:
                    variation = Variation.objects.get(product=product,
                                                      category__iexact=key,
                                                      value__iexact=value)
                    product_variation.append(variation)
                except Variation.DoesNotExist:
                    pass

        # Try to get the cart for the current session or create a new one.
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            # If the cart with does not exist, create a new cart.
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        item_already_in_cart = CartItem.objects.filter(
            product=product, cart=cart).exists()
        if item_already_in_cart:
            cart_item = CartItem.objects.filter(product=product, cart=cart)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            if product_variation in ex_var_list:
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(
                    product=product, quantity=1, cart=cart)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                quantity=1,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')


def remove(request, product_id, cart_item_id):
    '''
    Function based view to decrement quantity of product from the cart.
    '''
    try:
        # Try to fetch product, cart, cart_item for logged or non logged user
        product = Product.objects.get(id=product_id)
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(
                product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(
                product=product, cart=cart, id=cart_item_id)

    except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
        # If one of instances does not exist raise 404 error
        raise Http404

    # Check quantity of the cart item if it is greated then 1 subtract for one
    # If it is 1 delete from cart
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


def remove_item(request, product_id, cart_item_id):
    '''
    Function based view to handle removing product completely from the cart.
    '''
    try:
        # Try to fetch product, cart, cart_item for logged or non logged user
        product = Product.objects.get(id=product_id)
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(
                product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(
                product=product, cart=cart, id=cart_item_id)
    except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
        # If one of instances does not exist raise 404 error
        raise Http404

    # Delete fetched cart item
    cart_item.delete()

    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    '''
    Function based view to display cart with cart items
    '''
    # Initialize variables for tax and price without tax
    tax = 0
    price_without_tax = 0
    try:
        if request.user.is_authenticated:
            # Fetch all active items for logged in user
            cart_items = CartItem.objects.filter(
                user=request.user, is_active=True)
        else:
            # For non logged in users, fetch the cart ID from the session.
            cart = Cart.objects.get(cart_id=_cart_id(request))

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


@login_required(login_url='signin')
def checkout(request, total=0, quantity=0, cart_items=None):
    '''
    Function based view to display the checkout page with cart details.
    '''
    # Initialize variables for tax and price without tax
    tax = 0
    price_without_tax = 0
    try:
        if request.user.is_authenticated:
            # Fetch all active items for logged in user
            cart_items = CartItem.objects.filter(
                user=request.user, is_active=True)
        else:
            # For non logged in users, fetch the cart ID from the session.
            cart = Cart.objects.get(cart_id=_cart_id(request))

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
    template = 'cart/checkout.html'
    return render(request, template, context)
