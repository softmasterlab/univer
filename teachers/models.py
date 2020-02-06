from django.db import models
import departments.models as dm


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    subject = models.CharField(max_length=50)
    department = models.ForeignKey(dm.Department, on_delete=models.CASCADE)
