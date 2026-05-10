

from django import views
from django.contrib import admin
from django.urls import path
import secondapp.views

urlpatterns = [
    path('home/', secondapp.views.home, name='home'),
    path('about/', secondapp.views.about, name='about'),
    # path('home/', secondapp.views.home, name='home'),
    # path('about/', secondapp.views.about, name='about'),
    
]

