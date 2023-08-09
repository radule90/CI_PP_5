from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    '''
    Counts number of products in cart
    '''
    # Initialize cart count
    cart_count = 0
    # For admin panel returns empty dictionary
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            if request.user.is_authenticated:
                # Fetch cart items for logged in user
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                # Fetch cart items for non logged in user
                cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # Calculate total number of items in the cart
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            # When there is no cart return 0
            cart_count = 0
    return dict(cart_count=cart_count)
