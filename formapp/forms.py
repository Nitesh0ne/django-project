from django import forms

class EmployeeForm(forms.Form):
    eno = forms.IntegerField(label='Employee Number')
    ename = forms.CharField(label='Employee Name', max_length=100)
    esal = forms.FloatField(label='Employee Salary')
    eaddr = forms.CharField(label='Employee Address', max_length=200)
    