import re
from django import forms
from .models import Account, Profile
from phonenumber_field.formfields import PhoneNumberField


class SignupForm(forms.ModelForm):
    '''
    Sign up form with password control
    https://stackoverflow.com/questions/26823766/re-search-password-checking-error
    '''
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
        # Placeholders for form fields to display as hints in input fields
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'password': 'Password',
            'confirm_password': 'Confirm Password'
        }
        # Set placeholders and hide labels for each form field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

    def clean(self):
        # Custom validation method
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if password and confirm_password match
        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match!')

        # Check for strong password criteria
        # https://stackoverflow.com/questions/26823766/re-search-password-checking-error
        if not re.search('[0-9]', password) or \
           not re.search('[A-Z]', password) or \
           not re.search('[!@#$%^&*()_+{}:<>?]', password) or \
           len(password) < 6:
            self.add_error('password',
                           'Password must contain at least one number, '
                           'one capital letter, one special symbol, '
                           'and be at least 6 characters long.')

        return cleaned_data

    def save(self, commit=True):
        # Custom save method to handle user data
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email'].split("@")[0]
        user.password = self.cleaned_data['password']
        user.set_password(self.cleaned_data['password'])
        user.phone_number = self.cleaned_data['phone_number']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    '''
    Form to update account fields of profile
    '''
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Placeholders for form fields to display as hints in input fields
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }
        # Set placeholders and hide labels for each form field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False


class ProfileForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    class Meta:
        model = Profile
        fields = ('address_line_1', 'address_line_2', 'city', 'postcode',
                  'state', 'country')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # Placeholders for form fields to display as hints in input fields
        placeholders = {
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'postcode': 'Postcode',
            'state': 'State / County',
            'country': 'Country'
        }
        # Set placeholders and hide labels for each form field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
