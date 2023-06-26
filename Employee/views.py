from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def home(request):
    try:
        employee_obj = Employee.objects.all()
        serializer = EmployeeSerializer(employee_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    except:
        return Response('Invalid Employee')

@api_view(['POST'])
def post_employee(request):
    try:
        employee_obj = Employee.objects.all()
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    except:
        return Response({'status':400})

@api_view(['POST'])
def update_employee(request, id):
    try:
        employee_obj = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(instance=employee_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 200, 'payload': serializer.data})
    except:
        return Response({'status':400})

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee_obj = Employee.objects.get(id=id)
        employee_obj.delete()
        return Response('employee deleted')
    except:
        return Response('Invalid employee')