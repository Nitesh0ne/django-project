from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    hire_date = models.DateField()
    job_title= models.CharField(max_length=50)
    is_active= models.BooleanField(default=True)