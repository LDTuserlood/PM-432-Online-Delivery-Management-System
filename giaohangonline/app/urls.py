from django.contrib import admin
from django.urls import path
from . import views
from .views import placeorder

# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('placeorder/', views.placeorder, name="placeorder"),
]