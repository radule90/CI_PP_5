from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from .models import Account
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

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
            print(send_email)
            send_email.send()
            return redirect('account/signin/?command=verification&email='+recipient)

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
            login(request, user)
            messages.success(request, 'You have successfully signed in.')
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
