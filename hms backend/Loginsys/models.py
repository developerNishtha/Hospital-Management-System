from django.db import models

class Newuser(models.Model):
    Username=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    pwd=models.CharField(max_length=150)