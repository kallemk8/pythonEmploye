from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)

    def __str__(self) -> str:
        # return f"my name is {self.name} and my age is {self.age}"
        return self.name + " " + self.age
    

class Departments(models.Model):
    Title = models.CharField(max_length=200)
    Prasad = models.CharField(max_length=200)