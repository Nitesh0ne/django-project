from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm




def home(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EmployeeForm()
    context = {
        "employees" : employees,
        "form" : form
    }
    return render(request,'secondapp/home.html', context=context)



def buisness(request):

    return render(request, "secondapp/buisness.html")



def contact(request):
    count = int(request.COOKIES.get("count",0))
    newcount = count + 1
    context = { 'count':newcount }
    response = render(request,"secondapp/contact.html",context=context)
    response.set_cookie('count', newcount, max_age=60)
    return response


def portfolio(request):
    return render(request, "secondapp/portfolio.html")


def name_view(request):
    context = {}
    return render (request, 'secondapp/name.html', context=context)

def age_view(request):
    context = {}
    return render (request, 'secondapp/age.html', context=context)

def salary_view(request):
    context = {}
    return render (request, 'secondapp/salary.html', context=context)


def result_view(request):
    context = {}
    return render (request, 'secondapp/result.html', context=context)




