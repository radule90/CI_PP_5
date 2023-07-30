from django.shortcuts import render
from .forms import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()
    template = 'account/signup.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
