from django.contrib import admin
from .models import Product, Variation

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

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'category', 'value', 'is_active')
    list_editable = ('is_active',)
    search_fields = ['category', 'value',]
    list_filter = ('product', 'category', 'value', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
