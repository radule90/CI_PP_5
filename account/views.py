from django.shortcuts import render
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

    else:
        form = SignupForm()
    template = 'account/signup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
