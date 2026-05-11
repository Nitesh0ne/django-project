from django.shortcuts import render

def home(request):
    res='secondapp/home.html'
    return render(request, res)
