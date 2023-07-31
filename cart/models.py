from django.db import models
from product.models import Product, Variation
from account.models import Account

# Create your models here.


class Cart(models.Model):
    '''
    Cart model for storing items added by users during their shopping session.
    '''
    cart_id = models.CharField(max_length=250, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    '''
    CartItem model representing products added to a cart.
    '''
    user = models.ForeignKey(Account, on_delete=models.CASCADE,
                             related_name='cart_items', null=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cart_items')
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='cart_items', null=True)
    variations = models.ManyToManyField(Variation)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        '''
        Method to calculate the subtotal for each CartItem.
        '''
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.product_name
