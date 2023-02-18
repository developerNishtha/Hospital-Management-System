from django.db import models
from diagnosis.models import diagnosismodel

class diagnosis(models.Model):
    previousdiagnosis=models.CharField(max_length=500)
    finaldiagnosis=models.CharField(max_length=500)
    UHID=models.OneToOneField(diagnosismodel,on_delete=models.CASCADE,related_name='++')
    
    class Meta:
        db_table="diagnosis"

