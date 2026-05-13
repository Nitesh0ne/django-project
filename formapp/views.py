from django.shortcuts import render
from .forms import EmployeeForm


# Create your views here.
def employee_view(request):

   form = EmployeeForm()

   # if request.method == "POST":
   #    form = EmployeeForm(request.POST)
   #    if form.is_valid():
   #       print("Name: ", form.cleaned_data["ename"])
   #       # Employee.objects.create(ename=form.cleaned_data)

   context = {"form":form}
   # form.EmployeeForm()
   return render(request, "formapp/employeerecord.html",context=context)
