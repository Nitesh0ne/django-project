from django.contrib import admin
from .models import Employee


# Register your models here.    

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    list_per_page =1


# admin.site.register(Employee)




