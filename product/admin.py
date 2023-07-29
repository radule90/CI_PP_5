from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'category',
                    'stock', 'price', 'is_available')
    search_fields = ['product_name', 'description', 'price']
    list_display_links = ('product_name',)
    list_filter = ('product_name', 'category', 'price',
                   'is_available')
    list_editable = ('is_available',)


admin.site.register(Product, ProductAdmin)
