from django.contrib import admin
from django.urls import path, include
from subsidiary.views import *

urlpatterns = [
    path('', index),
    path('subs_1/', subs_1),
]
