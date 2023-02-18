from django.db import models

from homepage.models import homepagemodel

class opdcomplainmodel(models.Model):
    chiefcomplain=models.CharField(max_length=500)
    pastcomplain=models.CharField(max_length=500)
    followupvisit=models.CharField(max_length=500)
    opdcomplain_UHID=models.OneToOneField(homepagemodel,on_delete=models.CASCADE,related_name='++')
    
    
