from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('category/<slug:category_slug>/', views.shop,
         name='filter_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',
         views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('create_review/<int:product_id>/', views.create_review,
         name='create_review')
]
