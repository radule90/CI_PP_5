from django.shortcuts import render, redirect
from cart.models import CartItem
from .models import Order, OrderProduct, Payment
from .forms import OrderForm
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
import stripe


# Create your views here.


def payments(request):
    if request.method == "POST":
        # Retrieve the order id, payment id and status from the POST data
        order_id = request.POST.get('order_id')
        payment_id = request.POST.get('payment_id')
        payement_status = request.POST.get('status')


        # Retreive paid order
        order = Order.objects.get(user=request.user, id=order_id, is_ordered=False)
        print(order.id)

        # Creating and saving new Payment instance
        payment = Payment(
            user=request.user,
            payment_id=payment_id,
            payment_method="Stripe",
            amount_paid=order.order_total,
            status=payement_status
        )
        payment.save()

        return redirect('shop')


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
    # Loop through items in cart
    for cart_item in cart_items:
        # Calculate the total price, tax and product quantity in cart.
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity

        # Calculate tax and price without tax
        tax = round(((19 * total) / 100), 2)
        price_without_tax = total - tax

    if request.method == 'POST':
        # Check if methods is post and form data is valid
        form = OrderForm(request.POST)
        if form.is_valid():
            # Creates new instance of Order
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

            # Retreive new Order data
            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)

            # Create stripe payment intent 
            stripe.api_key = settings.STRIPE_SECRET_KEY
            intent = stripe.PaymentIntent.create(
                amount=round(total * 100),
                currency=settings.STRIPE_CURRENCY,
            )

            context = {
                'order': order,
                'cart_items': cart_items,
                'total': total,
                'tax': tax,
                'price_without_tax': price_without_tax,
                'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
                'client_secret': intent.client_secret,
                'order_id': order.id,
            }
            template = 'order/payments.html'
            return render(request, template, context)
        else:
            return redirect('checkout')
