from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, CartItem
from product.models import Product, Variation

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
    print(product)
    product_variation = []
    if request.method == 'POST':
        # Loop through the POST data to find variations and add them to the 'product variation list'.
        print('requeset post: ',request.POST)
        for item in request.POST:
            key = item
            print('key: ',key)
            value = request.POST[key]
            print('value: ',value)
            try:
                variation = Variation.objects.get(product=product,
                                                  category__iexact=key,
                                                  value__iexact=value)
                product_variation.append(variation)
                print('variation: ',variation)
                print('product variation: ',product_variation)
            except:
                pass

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        print('Cart: ',cart)
    except Cart.DoesNotExist:
        # If the cart with does not exist, create a new cart.
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()
    print('Cart: ',cart)
    
    item_already_in_cart = CartItem.objects.filter(product=product, cart=cart).exists()
    print(item_already_in_cart)
    if item_already_in_cart:
        cart_item = CartItem.objects.filter(product=product, cart=cart)
        print('cart_item: ',cart_item)
        ex_var_list = []
        id = []
        for item in cart_item:
            print('item ', item)
            existing_variation = item.variations.all()
            print('existing_variation ',existing_variation)
            ex_var_list.append(list(existing_variation))
            print('ex_var_list:',ex_var_list)
            id.append(item.id)
        print('ex_var_list:',ex_var_list)
        if product_variation in ex_var_list:
            index = ex_var_list.index(product_variation)
            print('index: ',index)
            item_id = id[index]
            print('item_id ',item_id)
            item = CartItem.objects.get(product=product, id=item_id)
            print('item: ',item)
            item.quantity += 1
            print('qty: ', item.quantity)
            item.save()
        else:
            item = CartItem.objects.create(
                product=product, quantity=1, cart=cart)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
                print(item.variations)
            item.save()
    else:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        print(cart_item)
        if len(product_variation) > 0:
            cart_item.variations.clear()
            print('Product Variations to Add:', product_variation)
            cart_item.variations.add(*product_variation)
            print('Product Variations to Add:', product_variation)
        cart_item.save()
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


def cart(request, total=0, quantity=0, cart_items=None):
    '''
    Function based view to display cart with cart items
    '''
    tax = 0
    price_without_tax = 0
    try:
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
