from dataclasses import fields
from pickle import FALSE
from pyexpat import model
from django import forms
from .models import employee


class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields=('fullname','mobile','emp_code','position')
        labels =        {
            'fullname':'Employee Name'


        }
    def __init__(self,*args,**kwargs):
        super(employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='select'
        self.fields['emp_code'].required=False


