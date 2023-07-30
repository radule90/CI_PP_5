from django.shortcuts import render

# Create your views here.

def signup(request):
    template = 'account/signup.html'
    return render(request, template)
