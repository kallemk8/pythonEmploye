from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics



class Employees_List(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

'''
    ==========All generics ===========

    createAPIView
    ListAPIview
    RetrieveAPIView
    DestroyAPIView
    UpdateAPIView

    ListCreateAPIView
    RetrieveUpdateAPIView
    RetrieveDestroyAPIView
    RetrieveUpdateDestroyAPIView

    =========Mixin Classes Action Metods

    ListModelMixin List()
    CreateModelMixin create()
    RetrieveModelMixin retrieve()
    UpdateModelMixin   update()
    DestroyModelMixin  Destory()


'''

class Employee_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

'''
class Employees_List(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
class Employee_Details(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''
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
'''