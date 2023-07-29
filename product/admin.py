from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('is_available', 'product_name',
                    'category', 'stock', 'price')
    search_fields = ['product_name', 'description', 'price']
    list_display_links = ('product_name', 'category',)


admin.site.register(Product, ProductAdmin)

