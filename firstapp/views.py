from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    context = {
        'f_name' : "Nitesh",
        'l_name' : "Nepali"
    }
    
    return render(request, "firstapp/index.html",context=context)

 