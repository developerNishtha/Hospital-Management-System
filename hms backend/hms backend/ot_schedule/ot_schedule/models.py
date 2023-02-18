from django.db import models

class ot_schedulemodel(models.Model):
    schedule_date=models.DateField(max_length=500)
    surgery_date=models.DateField(max_length=500)
    surgeon_name=models.CharField(max_length=500)
    surgery_start_time=models.TimeField(max_length=500)
    surgery_end_time=models.TimeField(max_length=500)
    ot_booked_by=models.CharField(max_length=500)
    schedule_status=models.CharField(max_length=500)
    procedure_name=models.CharField(max_length=500)
    notes=models.CharField(max_length=500)
    assistant1=models.CharField(max_length=500)
    assistant2=models.CharField(max_length=500)
    remarks=models.CharField(max_length=500)
    type_of_anasthesia=models.CharField(max_length=500)
    anastheiologist=models.CharField(max_length=500)
    requirements=models.CharField(max_length=500)
    
    class Meta:
        db_table="ot_schedule"

