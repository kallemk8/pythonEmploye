from django.shortcuts import render
from rest_framework import generics
from .models import Instructor, Course
from .serializers import InstructorSerializer, CourseSerializer
# Create your views here.

class Instructor_List(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
    
class Courses_List(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    
