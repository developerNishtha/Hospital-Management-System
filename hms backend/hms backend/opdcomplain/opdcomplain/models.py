from django.db import models

class opdcomplainmodel(models.Model):
    chiefcomplain=models.CharField(max_length=500)
    pastcomplain=models.CharField(max_length=500)
    followupvisit=models.CharField(max_length=500)
    
    class Meta:
        db_table="opdcomplain"

