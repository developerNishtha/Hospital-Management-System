from django.db import models
from diagnosis.models import Empmodel

class OPD_Examination(models.Model):
    local_examination=models.CharField(max_length=500)
    dre=models.CharField(max_length=500)
    systematic_examination=models.CharField(max_length=500)
    UHID=models.OneToOneField(Empmodel,on_delete=models.CASCADE,related_name='courseobj')
    
    

