from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order
from .forms import OrderForm
from django.utils import timezone


# Create your views here.


def place_order(request, quantity=0, total=0):
    '''
    Function based view to handle order placement
    Validates order form, calculates total price, tax
    Generate order number
    '''
    # Gettung the current user
    current_user = request.user

    # Retrieve all items in user cart and number of them
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    # Check if there are no items in cart
    if cart_count <= 0:
        return redirect('shop')

    tax = 0
    price_without_tax = 0
    for cart_item in cart_items:
        # Calculate the total price, tax and product quantity in cart.
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

        # Calculate tax and price without tax
        tax = round(((19 * total) / 100), 2)
        price_without_tax = total - tax

    if request.method == 'POST':
        # Check if methods is post and form data is submitted
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone_number']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            # Generate order number using the current date and order id
            order_number = timezone.now().strftime("%Y%m%d") + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('checkout')
    else:
        return redirect('checkout')
