from django import views
from django.contrib import admin
from django.urls import path
import secondapp.views

urlpatterns = [
    path('', secondapp.views.home, name='home'),
    path('students/', secondapp.views.student_list, name='student_list'),
]

