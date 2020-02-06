from django.db import models
import groups.models as gm


class Student(models.Model):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    rate = models.FloatField()
    group = models.ForeignKey(gm.Group, on_delete=models.CASCADE)
