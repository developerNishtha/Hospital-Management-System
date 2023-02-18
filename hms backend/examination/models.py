from django.db import models
from homepage.models import homepagemodel


class OPD_Examination(models.Model):
    local_examination=models.CharField(max_length=500)
    dre=models.CharField(max_length=500)
    systematic_examination=models.CharField(max_length=500)
    UHID=models.OneToOneField(homepagemodel,on_delete=models.CASCADE,related_name='++')
    
    

