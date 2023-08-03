from django.contrib import admin
from .models import Payment, Order, OrderProduct

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone_number', 'city',
                    'country', 'order_total', 'created_at', 'is_ordered']
    list_filter = ('is_ordered', 'status', 'country')
    search_fields = ['order_number', 'first_name', 'last_name', 'email']
    list_per_page = 10

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'payment_method', 'amount_paid', 'status'] 
    list_filter = ['status', 'payment_method']


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
