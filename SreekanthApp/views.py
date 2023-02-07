from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST'])
def Employees_List(request):
   if request.method == "GET":
    employees =  Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({"employeeList":serializer.data}, safe=False)
   if request.method == "POST":
     serializer = EmployeeSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', "DELETE"])     
def Employee_Details(request, id):
    try: 
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == "DELETE":
       employee.delete()
       return Response(status=status.HTTP_404_NOT_FOUND)