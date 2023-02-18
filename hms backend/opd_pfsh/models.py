from django.db import models
from homepage.models import homepagemodel


class opd_pfsh(models.Model):
    previous_medical_history=models.CharField(max_length=500)
    family_medical_history=models.CharField(max_length=500)
    opdpfsh_UHID=models.OneToOneField(homepagemodel,on_delete=models.CASCADE,related_name='+')
    
    
   
