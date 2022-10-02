from django.urls import path
from emp_reg import views

urlpatterns=[
    path('',views.home,name='home'),
    path('forms/',views.emp_form,name='forms'),
    path('forms/<int:id>/',views.emp_form,name='update'),

    path('list/',views.emp_list,name='list'),
    path('delete/<int:id>/',views.emp_del,name='delete')

]