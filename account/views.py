from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


@login_required(login_url = 'signin')
def signout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have successfully signed out.')
        return redirect('signin')
    template = 'account/signout_confirm.html'
    return render(request, template)
