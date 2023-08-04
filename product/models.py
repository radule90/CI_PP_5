from django.db import models
from django.utils.text import slugify
from category.models import Category
from django.urls import reverse
from account.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg
# Create your models here.


class Product(models.Model):
    '''
    Model represents product
    Model includes custom save method for slug field
    '''
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/product', blank=False)
    banner = models.ImageField(upload_to='banner/product', blank=True)
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["product_name", "created_at"]

    def get_absolute_url(self):
        '''
        Method to return product url
        '''
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def average_rating(self):
        '''
        Mehod that calculates average review for product
        '''
        reviews = Review.objects.filter(product=self, status=True).aggregate(
            average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    '''
    https://docs.djangoproject.com/en/4.2/topics/db/managers/
    Manager model for variation
    Filter variations based on category
    '''
    def sizes(self):
        return super(VariationManager, self).filter(category='size',
                                                    is_active=True)

    def colors(self):
        return super(VariationManager, self).filter(category='color',
                                                    is_active=True)

    def materials(self):
        return super(VariationManager, self).filter(category='material',
                                                    is_active=True)


class Variation(models.Model):
    '''
    Model represents product variations
    Variations are optional for products
    '''
    VARIATION_CATEGORY_CHOICES = (
        ('size', 'Size of the product'),
        ('color', 'Color of the product'),
        ('material', 'Material of the product'),)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.CharField(max_length=50,
                                choices=VARIATION_CATEGORY_CHOICES)
    value = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.value


class Review(models.Model):
    '''
    Model represents product review with rating system
    '''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20, blank=True)
    review = models.TextField(blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0),
                               MaxValueValidator(5.0)], default=0.0)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.rating}"
