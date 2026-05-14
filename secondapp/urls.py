from django import views
from django.contrib import admin
from django.urls import path
import secondapp.views

urlpatterns = [
    # path('', secondapp.views.home, name='home'),
    path('', secondapp.views.home, name='home'),
    path('buisness/', secondapp.views.buisness, name='buisness'),
    path('contact/', secondapp.views.contact, name='contact'),
    path('portfolio/', secondapp.views.portfolio, name='portfolio'),
]

