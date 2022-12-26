from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=10)

class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    duration=models.IntegerField()
    fee=models.IntegerField()

    def _str_(self) :
        return self.name   

class Staff(models.Model):
    name1=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=15)
    phno=models.CharField(max_length=10)
    day=models.CharField(max_length=10)
    month=models.CharField(max_length=20)
    year=models.CharField(max_length=10)
    radio=models.CharField(max_length=20)

    def __str__(self):
        return self.name
