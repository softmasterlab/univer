from django.db import models
import faculties.models as fm


class Department(models.Model):
    title = models.CharField(max_length=150)
    about = models.TextField(max_length=300)
    content = models.TextField(max_length=1024)
    faculty = models.ForeignKey(fm.Faculty, on_delete=models.CASCADE)
