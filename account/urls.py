from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_validation/<uidb64>/<token>/', views.password_reset_validation, name='password_reset_validation'),
    path('set_new_password/', views.set_new_password, name='set_new_password'),
]
