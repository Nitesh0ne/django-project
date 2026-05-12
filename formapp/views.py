from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def form_index(request):
    form = EmployeeForm()
    context = {'form': form}

    return render(request, 'formapp/employeerecord.html.html', context=context)



def employee_input(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'formapp/success.html')
    else:
        form = EmployeeForm()
    context = {'form': form}
    return render(request, 'formapp/employeerecord.html', context=context)