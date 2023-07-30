from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def shop(request, category_slug=None):
    '''
    Function based view to list products in shop
    And filter products by category
    '''
    category = None
    products = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    template = 'product/shop.html'
    context = {
        'products': products,
        'category': category,
    }
    return render(request, template, context)