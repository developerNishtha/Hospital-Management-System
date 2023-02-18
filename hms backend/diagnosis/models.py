from django.db import models
from homepage.models import homepagemodel

class Empmodel(models.Model):
    previousdiagnosis=models.CharField(max_length=500)
    finaldiagnosis=models.CharField(max_length=500)
    diagnosis_UHID=models.OneToOneField(homepagemodel,on_delete=models.CASCADE,related_name='++')
    
   
