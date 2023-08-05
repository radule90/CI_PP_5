from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserProfileForm, ProfileForm
from .models import Account, Profile
from cart.models import Cart, CartItem
from cart.views import _cart_id
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from order.models import Order, OrderProduct
import requests
# Create your views here.


def signup(request):
    '''
    Fucntion based to register account and profile
    '''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create Profile automaticly
            profile = Profile()
            profile.user_id = user.id
            profile.save()

            # Activation Email
            current_site = get_current_site(request)
            mail_subject = 'Please Confirm Your E-mail Address'
            message = render_to_string('account/signup_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            recipient = form.cleaned_data.get('email')
            send_email = EmailMessage(mail_subject, message, to=[recipient])
            send_email.send()
            return redirect('/account/signin/?command=verification&email='+recipient)

    else:
        form = SignupForm()
    template = 'account/signup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                item_already_in_cart = CartItem.objects.filter(cart=cart).exists()
                if item_already_in_cart:
                    cart_items = CartItem.objects.filter(cart=cart)
                    # Retrieve variations of product
                    product_variation = []
                    for cart_item in cart_items:
                        variation = cart_item.variations.all()
                        product_variation.append(list(variation))

                    # Retrieve user product variations
                    cart_items = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for cart_item in cart_items:
                        existing_variation = cart_item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(cart_item.id)

                    #
                    for product in product_variation:
                        if product in ex_var_list:
                            index = ex_var_list.index(product)
                            cart_item_id = id[index]
                            cart_item = CartItem.objects.get(id=cart_item_id)
                            cart_item.quantity += 1
                            cart_item.user = user
                            cart_item.save()
                        else:
                            cart_items = CartItem.objects.filter(cart=cart)
                            for cart_item in cart_items:
                                cart_item.user = user
                                print(cart_item.user)
                                cart_item.save()
            except Cart.DoesNotExist:
                pass
            login(request, user)
            messages.success(request, 'You have successfully signed in.')
            url = request.META.get('HTTP_REFERER')
            try:
                # https://stackoverflow.com/questions/28328890/python-requests-extract-url-parameters-from-a-string
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    next_page = params['next']
                    return redirect(next_page)
            except:
                return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')
    template = 'account/signin.html'
    context = {
    }
    return render(request, template, context)


@login_required(login_url='signin')
def signout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have successfully signed out.')
        return redirect('signin')
    template = 'account/signout_confirm.html'
    return render(request, template)


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Welcome to Sun & Peaches! Your account has been activated successfully.')
        return redirect('signin')
    else:
        messages.error(request, 'The account activation link is invalid or has expired.')
        return redirect('signup')


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('account/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            recipient = email
            send_email = EmailMessage(mail_subject, message, to=[recipient])
            send_email.send()
            messages.success(request, 'An email has been sent to your account with instructions to reset your password.')
            return redirect('signin')
        else:
            messages.error(request, 'There is no account associated with this email address.')
            return redirect('password_reset')
    template = 'account/password_reset.html'
    return render(request, template)


def password_reset_validation(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Reset Your Password')
        return redirect('set_new_password')
    else:
        messages.error(request, 'The password reset link is invalid or has expired.')
        return redirect('password_reset')


def set_new_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Your password has been updated successfully.')
            return redirect('signin')
        else:
            messages.error(request, 'Password and confirm password do not match.')
            return redirect('set_new_password')
    else:
        template = 'account/set_new_password.html'
        return render(request, template)


def dashboard(request):
    orders = Order.objects.order_by('-created_at').filter(user_id=request.user.id, is_ordered=True)
    orders_count = orders.count()
    template = 'account/dashboard.html'
    context = {
        'orders_count': orders_count,
        'dashboard_active': 'dashboard_active',
    }
    return render(request, template, context)


def user_orders(request):
    '''
    Function based view displays list of orders for the current user.
    '''
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by('-created_at')
    template = 'account/user_orders.html'
    context = {
        'user_orders_active': 'user_orders_active',
        'orders': orders,
    }
    return render(request, template, context)


def order_details(request, order_id):
    order_detail = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_detail:
        subtotal += i.product_price * i.quantity
    template = 'account/order_details.html'
    context = {
        'user_orders_active': 'user_orders_active',
        'order_detail': order_detail,
        'order': order,
        'subtotal': subtotal,
    }
    return render(request, template, context)


def update_profile(request):
    '''
    Function based view to update user profile data
    '''
    # Get profile of request user
    user_profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('update_profile')
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=user_profile)
    template = 'account/update_profile.html'
    context = {
        'user_profile_active': 'user_profile_active',
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,
    }
    return render(request, template, context)


def password_change(request):
    '''
    Function-based view to handle password changes for authenticated users. 
    '''
    if request.method == 'POST':
        # Get current, new and confirmed new password
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Get current logged in user
        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            # Verify current password of the user and set new
            success = user.check_password(password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been updated successfully.')
                return redirect('signin')
            else:
                messages.error(request, 'The old password is incorrect.')
        else:
            messages.error(request, 'New password and Confirm password does not match.')
            return redirect('password_change')

    template = 'account/password_change.html'
    context = {
        'change_password_active': 'change_password_active',
    }
    return render(request, template, context)