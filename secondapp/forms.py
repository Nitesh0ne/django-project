from django import forms
from .models import Employee

#model form

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"



