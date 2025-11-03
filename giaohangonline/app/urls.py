from django.contrib import admin
from django.urls import path
from . import views
from .views import placeorder
from .views import tracuudonhang
from django.urls import path
from .views import order_management
from .views import order_management, complete_order, update_order_status

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
]