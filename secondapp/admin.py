from django.contrib import admin
from secondapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade')
    
admin.site.register(Student, StudentAdmin)

