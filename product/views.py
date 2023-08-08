from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from .models import Product, Review
from .forms import ReviewForm
from category.models import Category
from django.core.paginator import Paginator
from order.models import OrderProduct
from django.contrib.auth.decorators import login_required

# Create your views here.


def shop(request, category_slug=None):
    '''
    Function based view to list products in shop
    And filter products by category
    Gives number of products in shop or category
    '''
    # Initializinz category and products
    category = None
    products = None
    if category_slug is not None:
        # If a category slug is provided in the URL, get category object
        category = get_object_or_404(Category, slug=category_slug)

        # Filter products by the selected category that are available
        products = Product.objects.filter(category=category, is_available=True)

        # Paginator setup
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        # Count number of available products for category
        product_count = products.count()
    else:
        # If no category slug is provided, get all available products
        products = Product.objects.all().filter(is_available=True)

        # Paginator setup
        paginator = Paginator(products, 10)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        # Count number of all available products
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
        # Try to fetch product with category slug and product slug
        product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)
    except Product.DoesNotExist:
        # If the product doesn't exist, raise a 404 error
        raise Http404('Product does not exist!')

    # Check if the user has bought product, so that can leave review
    if request.user.is_authenticated:
        try:
            # Checking if user has bought that product
            order_product = OrderProduct.objects.filter(
                user=request.user, product_id=product.id).exists()
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
    # Initializinz products, product_count and page_obj
    products = None
    product_count = 0
    page_obj = None
    if 'q' in request.GET:
        # Check if q parameter is present in the GET request
        query = request.GET['q']
        if query:
            # If a q is present, perform search on various fields
            products = Product.objects.filter(
                Q(product_name__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query))
            # Count the number of search results
            product_count = products.count()

            # Paginator setup
            paginator = Paginator(products, 10)
            page = request.GET.get('page')
            page_obj = paginator.get_page(page)

    template = 'product/shop.html'

    context = {
        'products': page_obj,
        'product_count': product_count,
    }
    return render(request, template, context)


@login_required(login_url='signin')
def create_review(request, product_id):
    '''
    Function based view to create or update review for a product.
    '''
    # Get the URL of the previous page (referrer)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            # If user already left review, then update existing
            review = Review.objects.get(
                user__id=request.user.id, product__id=product_id)
            # Update the existing review and send success message
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
                # Display a success message and redirect to the referrer URL
                messages.success(request, 'Review created successfully.')
                return redirect(url)


@login_required(login_url='signin')
def delete_review(request, review_id):
    '''
    Function based view to delete a review
    '''
    # Get the URL of the previous page (referrer)
    url = request.META.get('HTTP_REFERER')

    try:
        # Get the review to be deleted if belongs to logged in user
        review = Review.objects.get(id=review_id, user=request.user)
        if request.method == 'POST':
            # Delete the review and show success message
            review.delete()
            messages.success(request, 'Review deleted successfully.')
            return redirect(review.product.get_absolute_url())
    except Review.DoesNotExist:
        # If review doesnt exist or doesn't belong to user, show error message
        messages.error(
            request,
            'Review not found or you do not have permission to delete it.')
    template = 'product/delete_review_confirm.html'
    context = {
        'previous_url': url,
    }
    return render(request, template, context)
