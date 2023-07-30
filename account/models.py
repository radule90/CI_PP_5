from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class MyAccountManager(BaseUserManager):
    '''
    Custom user manager to handle user creation.
    https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
    '''
    def create_user(self, first_name, last_name, username, email, password=None):
        '''
        Method to create regular user
        '''
        if not email:
            raise ValueError('Please provide a valid email address.')

        if not username:
            raise ValueError('A username is required.')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        '''
        Method for creating superuser
        '''
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    '''
    Custom user model
    https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
    '''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField()
    
    # Mandatory Django Fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Login with email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def full_name(self):
        '''
        Method to get full name
        '''
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        '''
        Mandatory by Django
        Check if user hase specific permission
        '''
        return self.is_admin

    def has_module_perms(self, add_label):
        '''
        Mandatory by Django
        Check if user hase specific permission for certain modul
        '''
        return True
