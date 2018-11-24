from django.db import models

# Create your models here.

class login(models.Model):
    LoginID = models.CharField(max_length=20)
    Password = models.CharField(max_length=25)
    UserID = models.CharField(max_length=12)
