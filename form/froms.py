from django import forms
from django.core import validators

class EmployeeForm (forms.Form):
    ename = forms.CharField()
    eaddr = forms.CharField()
    eno = forms.IntegerField()
    esal = forms.FloatField()

    # def clean_ename(self):
    #     inputname = self.changed_data['ename']
    #     if len(inputname) < 5:
    #         raise forms.ValidationError("The minimum number of Employee name should be greater than 5. ")
    #     return inputname

    # def clean_eaddr(self):
    #     inputaddr = self.changed_data['eaddr']
    #     if inputaddr != "kathmandu":
    #         raise forms.ValidationError("The address should  be in kathmandu")
    #     return inputaddr
    
    # def clean_eno(self):
    #     inputno = self.changed_data['eno']
    #     if len(inputno) > 10:
    #         raise forms.ValidationError("The Number should be exactly 10 digit")
    #     return inputno

    # def clean_esal(self):
    #     inputsal = self.changed_data['esal']
    #     if inputsal < 50000:
    #         raise forms.ValidationError("The salary should be less than 50000")
    #     return inputsal