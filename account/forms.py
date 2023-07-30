from django import forms
from .models import Account
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone_number = PhoneNumberField(help_text='Required')

    class Meta:
        model = Account
        fields = ('email', 'password', 'first_name', 'last_name',
                  'phone_number',)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
