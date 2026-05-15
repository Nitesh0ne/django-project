from django import forms
from .models import Employee

#model form

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        
class NameForm(forms.Form):
    name= forms.CharField()

    

class AgeForm(forms.Form):
    age=forms.IntegerField()



class Salaryorms.Form):
    age=forms.IntegerField()


class AgeForm(forms.Form):
    age=forms.IntegerField()
