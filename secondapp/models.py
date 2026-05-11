from django.db import models
# Create your models here.
class Student(models.Model):
    std_roll_no = models.IntegerField()
    std_fname = models.CharField(max_length=30)
    std_lname = models.CharField(max_length=30)
    std_class = models.IntegerField()
    
