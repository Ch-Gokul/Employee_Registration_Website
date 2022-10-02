from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import employee

from emp_reg.forms import employeeform
 
# Create your views here.
def home(request):
    return render(request,'base.html')
def emp_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form =employeeform()
        else:
            emp=employee.objects.get(pk=id)
            form=employeeform(instance=emp) 
        return render(request,'emp_form.html',{'form':form}) 
    else:
        if id==0:
            form =employeeform(request.POST)
        else:
            emp=employee.objects.get(pk=id)
            form=employeeform(request.POST,instance=emp) 
        
        if form.is_valid():
            form.save()
        return redirect('list')


def emp_list(request):
    context= {'emp_list':employee.objects.all()}
    return render(request,'emp_list.html',context)
def emp_del(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('list')
    
