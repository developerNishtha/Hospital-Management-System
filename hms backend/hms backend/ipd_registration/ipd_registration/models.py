from django.db import models

class ipd_registration(models.Model):
    registration_time=models.CharField(max_length=500)
    registration_date=models.CharField(max_length=500)
    patient_category=models.CharField(max_length=500)
    
    class Meta:
        db_table="ipd_registration"

