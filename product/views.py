from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def shop(request, category_slug=None):
    '''
    Function based view to list products in shop
    And filter products by category
    Gives number of products in shop or category
    '''
    category = None
    products = None
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    template = 'product/shop.html'
    context = {
        'products': products,
        'category': category,
        'product_count': product_count,
    }
    return render(request, template, context)