

from django import views
from django.contrib import admin
from django.urls import path
import secondapp.views

urlpatterns = [
    path('', secondapp.views.home, name='home'),
]

