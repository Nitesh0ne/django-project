# from django.shortcuts import render

from django.http import HttpResponse



def home(request):
    return HttpResponse("This is home page of second app")


def about(request):
    return HttpResponse("This is about page of second app")