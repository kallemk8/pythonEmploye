from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Departments
from .DepartmentSerializers import DepartmentSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
@api_view(['GET', 'POST'])
def Department_List(request):
   if request.method == "GET":
    employees =  Departments.objects.all()
    serializer = DepartmentSerializer(employees, many=True)
    return JsonResponse({"DepartmentList":serializer.data}, safe=False)
   if request.method == "POST":
     serializer = DepartmentSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)