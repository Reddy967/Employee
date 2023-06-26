from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=50)
    addressDetails = models.JSONField()
    WorkExperience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.ImageField()
