from django.db import models

class ot_schedulemodel(models.Model):
    schedule_date=models.DateField()
    surgery_date=models.DateField()
    surgeon_name=models.CharField(max_length=50)
    surgery_start_time=models.TimeField()
    surgery_end_time=models.TimeField()
    ot_booked_by=models.CharField(max_length=50)
    schedule_status=models.CharField(max_length=50)
    procedure_name=models.CharField(max_length=100)
    notes=models.CharField(max_length=500)
    assistant1=models.CharField(max_length=50)
    assistant2=models.CharField(max_length=50)
    remarks=models.CharField(max_length=500)
    type_of_anasthesia=models.CharField(max_length=500)
    anastheiologist=models.CharField(max_length=50)
    requirements=models.CharField(max_length=500)
    
    class Meta:
        db_table="ot_schedule"

