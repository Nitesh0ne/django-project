import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') # to set the environment variable
import django
django.setup() # to setup the django environment
from faker import *
from random import * 

from firstapp.models import Employee

faker = Faker("ne_NP") #  object created of the class Faker

def populate(n):
    for i in range(n):
        fno= randint(1000,200000)
        fname = faker.name()
        fsal = round(uniform(10000,50000),2)
        faddr = faker.city()
        emp_record = Employee.objects.get_or_create(eno=fno,ename=fname,esal=fsal,eaddr=faddr)



populate(10)


