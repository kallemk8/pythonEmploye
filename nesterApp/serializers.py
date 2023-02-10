from rest_framework import serializers

from .models import Instructor, Course



class InstructorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Instructor
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer()
    class Meta:
        model = Course
        fields = "__all__"