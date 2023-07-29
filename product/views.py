from django.shortcuts import render
from .models import Product

# Create your views here.
def shop(request):
    products = Product.objects.all().filter(is_available=True)

    template = 'product/shop.html'
    context = {
        'products': products,
    }
    return render(request, template, context)