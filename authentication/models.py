from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


class ExcelData(models.Model):
    data = models.JSONField()



