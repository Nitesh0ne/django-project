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
    return render(request,"secondapp/contact.html")


def portfolio(request):
    return render(request, "secondapp/portfolio.html")

