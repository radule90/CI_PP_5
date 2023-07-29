from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    '''
    Model represents category
    Model includes custom save method for slug field
    '''
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['category_name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        '''
        Auto populate slug field solution found on:
        https://learndjango.com/tutorials/django-slug-tutorial
        '''
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name
