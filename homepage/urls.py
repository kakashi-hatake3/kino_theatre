from django.contrib import admin
from django.urls import path, include
from homepage.views import *
urlpatterns = [
    path('', index),
]
