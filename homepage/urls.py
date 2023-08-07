from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
