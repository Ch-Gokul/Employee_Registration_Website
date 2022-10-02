from turtle import position, title
from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title
class employee(models.Model):
    fullname= models.CharField(max_length=30)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=10)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)


