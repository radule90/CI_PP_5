from django import forms
from .models import Account
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)
    phone_number = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'email', 
                'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'password': 'Password',
            'confirm_password': 'Confirm Password'
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
