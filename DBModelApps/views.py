from django.shortcuts import render
from DBModelApps.models import Employee
def empdata(request):
    emplist=Employee.objects.all()
    dict={'emplist':emplist}
    return render(request,'DBModelApp/emp.html',context=dict);
# Create your views here.
