from django.contrib import admin
from DBModelApps.models import Employee
#admin.site.register(Employee)
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr'];

admin.site.register(Employee,EmployeeAdmin);


from DBModelApps.models import Job
admin.site.register(Job)