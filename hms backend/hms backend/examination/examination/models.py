from django.db import models

class OPD_Examination(models.Model):
    local_examination=models.CharField(max_length=500)
    dre=models.CharField(max_length=500)
    systematic_examination=models.CharField(max_length=500)
    
    class Meta:
        db_table="opd_examination"

