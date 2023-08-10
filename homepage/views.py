from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Subscriber
from .forms import NewsletterForm
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import user_passes_test, login_required
from product.models import Product
from django.http import Http404

# Create your views here.


def homepage(request):
    '''
    Function based view for the homepage.
    Retrieves products with banner images and renders the homepage
    '''
    try:
        products_with_banner = Product.objects.exclude(banner='')
    except Product.DoesNotExist:
        raise Http404
    template = 'homepage/index.html'
    context = {
        'active_homepage': 'active_homepage',
        'products_with_banner': products_with_banner,
    }
    return render(request, template, context)


def subscribe(request):
    '''
    Function based view to handle user subscription
    '''
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')

        # Check if there is empty input
        if not full_name or not email:
            messages.error(request, 'Both name and email are required.')
            return redirect('homepage')

        # Check if already exsists
        if Subscriber.objects.filter(email=email).exists():
            messages.error(
                request, 'You are already subscribed to our newsletter.')
            return redirect('homepage')

        # Validate email
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect('homepage')

        subscriber = Subscriber()
        subscriber.full_name = full_name
        subscriber.email = email
        subscriber.save()
        messages.success(
            request, 'You have successfully subscribed to our newsletter.')
        return redirect('homepage')


def is_admin(user):
    '''
    Function to check if user is admin
    '''
    return user.is_authenticated and user.is_admin

@login_required(login_url='signin')
@user_passes_test(is_admin)
# Check if use is admin and logged in
def newsletter(request):
    '''
    Function based view to handle newsletter
    '''
    # Chek for post method and validate form
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            recipients = form.cleaned_data.get('recipients').split(',')
            message_body = form.cleaned_data.get('message_body')
            newsletter = EmailMessage(subject, message_body, to=recipients)
            newsletter.content_subtype = 'html'
            if newsletter.send():
                messages.success(
                    request, 'You have successfully sent the newsletter.')
            else:
                messages.error(
                    request, 'There was an error sending the newsletter.')
    # Render newsletter form on page
    form = NewsletterForm()
    subscribers = Subscriber.objects.all()
    form.fields['recipients'].initial = ','.join(
        sub.email for sub in subscribers)
    template = 'homepage/newsletter.html'
    context = {
        'form': form,
        'newsletter_active': 'newsletter_active',
    }
    return render(request, template, context)
