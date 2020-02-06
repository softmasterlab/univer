from django.db import models
import faculties.models as fm


class Group(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(fm.Faculty, on_delete=models.CASCADE)
