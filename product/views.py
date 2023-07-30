from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import Http404
from .models import Product
from category.models import Category
from django.core.paginator import Paginator


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

        # Paginator setup
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)

        # Paginator setup
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        product_count = products.count()

    template = 'product/shop.html'
    context = {
        'products': page_obj,
        'category': category,
        'product_count': product_count,
        'active_shop': 'active_shop',
    }
    return render(request, template, context)


def product_detail(request, category_slug, product_slug):
    '''
    Function based view to display product details.
    Gets product by category slug and product slug
    If not found raise 404 error
    '''
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Product.DoesNotExist:
        raise Http404('Product does not exist!')
        
    template = 'product/product_detail.html'
    context = {
        'product': product,
        'active_shop': 'active_shop',
    }
    return render(request, template, context)


def search(request):
    '''
    Function based view to handle product search
    '''
    products = None
    product_count = 0
    page_obj = None
    if 'q' in request.GET:
        query = request.GET['q']
        if query:
            products = Product.objects.filter(
                Q(product_name__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query))
            product_count = products.count()

            # Paginator setup
            paginator = Paginator(products, 1)
            page = request.GET.get('page')
            page_obj = paginator.get_page(page)
    
    template = 'product/shop.html'

    context = {
        'products': page_obj,
        'product_count': product_count,
    }
    return render(request, template, context)
