from django.db import models

class Student(models.Model):
    std_roll_no = models.IntegerField()
    std_fname = models.CharField(max_length=30)
    std_lname = models.CharField(max_length=30)
    std_class = models.IntegerField()

    # REQUIRED fields (safe because new DB)
    std_section = models.CharField(max_length=30, default="A")

    # OPTIONAL fields
    std_dob = models.DateField(null=True, blank=True)
    std_email = models.EmailField(null=True, blank=True)
    std_phone_no = models.CharField(max_length=15, null=True, blank=True)

    # SAFE DEFAULT
    std_address = models.TextField(default="Unknown")

    def __str__(self):
        return f"{self.std_fname} {self.std_lname}"