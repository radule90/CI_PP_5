from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add, name='add'),
    path('remove/<int:product_id>/<int:cart_item_id>/', views.remove, name='remove'),
    path('remove_item/<int:product_id>/', views.remove_item,
         name='remove_item'),
]
