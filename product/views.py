from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from .models import Product, Review
from .forms import ReviewForm
from category.models import Category
from django.core.paginator import Paginator
from order.models import OrderProduct

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
    
    # Check if the user has bought product, so that can leave review
    if request.user.is_authenticated:
        try:
            order_product = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()
        except OrderProduct.DoesNotExist:
            order_product = None
    else:
        order_product = None

    # Get all reviews for the product
    reviews = Review.objects.filter(product_id=product.id, status=True)

    template = 'product/product_detail.html'
    context = {
        'product': product,
        'active_shop': 'active_shop',
        'order_product': order_product,
        'reviews': reviews,
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


def create_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
        # If user already left review, then update existing
            review = Review.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect(url)
        except Review.DoesNotExist:
        # If user didn't leave review, create new
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = Review()
                review.subject = form.cleaned_data['subject']
                review.review = form.cleaned_data['review']
                review.rating = form.cleaned_data['rating']
                review.ip = request.META.get('REMOTE_ADDR')
                review.product_id = product_id
                review.user_id = request.user.id
                review.save()
                messages.success(request, 'Review created successfully.')
                return redirect(url)
