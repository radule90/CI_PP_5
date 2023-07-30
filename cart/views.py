from django.shortcuts import render

# Create your views here.


def cart(request):
    context = {}
    template = 'cart/cart.html'
    return render(request, template, context)
