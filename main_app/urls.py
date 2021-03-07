from django.urls import path,include
from django.contrib import admin
from main_app import views
urlpatterns = [
    path('', views.enter,name='Inputs'),
]