from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm
from .models import Account
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up!')
            return redirect('signup')

    else:
        form = SignupForm()
    template = 'account/signup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def signin(request):
    template = 'account/signin.html'
    context = {
    }
    return render(request, template, context)