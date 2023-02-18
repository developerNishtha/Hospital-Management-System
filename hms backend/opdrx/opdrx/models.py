from django.db import models

class opdrxmodel(models.Model):
    medicinename=models.CharField(max_length=50)
    doctorname=models.CharField(max_length=50)
    dosage=models.CharField(max_length=50)
    route=models.CharField(max_length=50)
    entreperiod=models.CharField(max_length=50)
    duration=models.CharField(max_length=50)
    total=models.CharField(max_length=50)
    followupinstruction=models.CharField(max_length=500)
    todaydate=models.DateField()
    todaytime=models.TimeField()
    nextfollowupdate=models.DateField()
    nextfollowuptime=models.TimeField()
    class Meta:
        db_table="opdrx"

