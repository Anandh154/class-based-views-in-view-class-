from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()