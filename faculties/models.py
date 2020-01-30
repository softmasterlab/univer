from django.db import models


class Faculty(models.Model):
    title = models.CharField(max_length=150)
    about = models.TextField(max_length=300)
    content = models.TextField(max_length=1024)
    picture = models.FileField(upload_to='pictures/')
    photo = models.FileField(upload_to='photo/')
    site = models.URLField()
