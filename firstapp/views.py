from django.shortcuts import render
from firstapp.models import Employee

# import datetime
# def home(request):
#     # context = {
#     #      name : "nitesh",
#     #     age : 20
#     # }
#     date = datetime.datetime.now()
#     msg= "Hello Guest !!!! "
#     h= int(date.strftime("%H"))
#     if h < 12:
#         msg += "Good Morning"
#     elif h < 16:
#         msg += "Good Afternoon"
#     elif h < 20:
#         msg += "Good Evening"
#     else:
#         msg += "Good Night"
#     context = {'insert_date': date, 'insert_msg': msg}
#     return render(request, 'firstapp/html/index.html', context=context)

def home(request):
    res='firstapp/home.html'
    return render(request, res)

# def home(request):
#     res = "<h1>This is home page</h1>"
#     return HttpResponse(res)

def index(request):
    # context = {
    #     'name': "Nitesh",
    #     'age': 20
    # }
    emp_list = Employee.objects.all()
    context = {'emp_list':emp_list}

    return render(request, 'firstapp/index.html', context=context)

def network(request):
    return render(request, 'firstapp/network.html')

def system(request):
    res='firstapp/system.html'
    return render(request, res)

def cloud(request):
    res='firstapp/cloud.html'
    return render(request, res)

def devops(request):
    res='firstapp/devops.html'
    return render(request, res)

def cybersecurity(request):
    res='firstapp/cybersecurity.html'
    return render(request, res)


    



    






