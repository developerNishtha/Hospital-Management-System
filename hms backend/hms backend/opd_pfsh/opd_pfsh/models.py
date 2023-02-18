from django.db import models

class opd_pfsh(models.Model):
    previous_medical_history=models.CharField(max_length=500)
    family_medical_history=models.CharField(max_length=500)
    
    
    class Meta:
        db_table="opd_pfsh"

