from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'email', 'age', 'gender', 'PhoneNumber', 'addressDetails', 'WorkExperience', 'qualifications', 'projects', 'photo')