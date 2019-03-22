from django.db import models


# Create your models here.
class abc(models.Model):
    empid = models.TextField(max_length=50)
    empname = models.CharField(max_length=50, default="abc")

class post(models.Model):
    name=models.TextField()
    text = models.TextField(max_length=50)
    content   = models.CharField(max_length=50, default="abc")

