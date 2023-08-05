from django import forms
from .models import Account, Profile
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match!')

        return cleaned_data

    def save(self, commit=True):
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
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }

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
        placeholders = {
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'postcode': 'Postcode',
            'state': 'State / County',
            'country': 'Country'
        }
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False