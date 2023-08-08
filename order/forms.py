from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    '''
    Form for the order model to get order details from user
    '''
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'address_line_1', 'address_line_2', 'city', 'postcode',
                  'state', 'country', 'order_note']
