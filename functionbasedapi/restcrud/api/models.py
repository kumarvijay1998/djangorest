from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    roll=models.CharField(max_length=10)
    city=models.CharField(max_length=10)