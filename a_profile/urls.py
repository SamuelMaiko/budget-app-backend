from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileView.as_view(), name='my-profile'),
]
