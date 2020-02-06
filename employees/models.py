from django.db import models
import departments.models as dm


class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    position = models.TextField(max_length=50)
    department = models.ForeignKey(dm.Department, on_delete=models.CASCADE)
