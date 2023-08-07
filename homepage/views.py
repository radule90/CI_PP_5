from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Subscriber


# Create your views here.


def homepage(request):
    template = 'homepage/index.html'
    context = {
        'active_homepage': 'active_homepage',
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
            messages.error(request, 'You are already subscribed to our newsletter.')
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
        messages.success(request, 'You have successfully subscribed to our newsletter.')
        return redirect('homepage')


def newsletter(request):
    return redirect('homepage')
