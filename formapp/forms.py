from django import forms
from django.core import validators


def starts_with_v(value):
    if value[0].lower() != 'v':
        raise forms.ValidationError("Name should start with v. ")
    



class EmployeeForm(forms.Form):
    ename = forms.CharField(validators=[starts_with_v]) 
    eaddr = forms.CharField()
    eno = forms.IntegerField()
    esal = forms.FloatField()

    # validation done by programmer using clean method 
    # def clean_ename(self):
    #     input_name = self.cleaned_data['ename']
    #     if len(input_name) < 5 :
    #         raise  forms.ValidationError("The minimum number of employee name should be greater than 5")
    #     return input_name

