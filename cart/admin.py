from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'created_at')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'is_active', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display_links = ('product',)
    list_filter = ('cart', 'is_active', 'product',)
    list_editable = ('is_active',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
