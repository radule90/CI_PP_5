from django.db import models
from django.utils.text import slugify
from category.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    '''
    Model represents product
    Model includes custom save method for slug field
    '''
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='products')
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
