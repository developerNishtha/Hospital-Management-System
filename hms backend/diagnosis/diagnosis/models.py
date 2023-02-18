from django.db import models

class Empmodel(models.Model):
    previousdiagnosis=models.CharField(max_length=500)
    finaldiagnosis=models.CharField(max_length=500)
    
    class Meta:
        db_table="diagnosis"

