from django.db import models

class round_notesmodel(models.Model):
    round_note_number=models.CharField(max_length=20)
    rn_date=models.DateField()
    rn_time=models.TimeField()
    rmo_dr_name=models.CharField(max_length=50)
    dr_name=models.CharField(max_length=50)
    visit_type=models.CharField(max_length=50)
    symptons=models.CharField(max_length=500)
    examination=models.CharField(max_length=500)
    nursing_advise=models.CharField(max_length=500)
    lab_test_order=models.CharField(max_length=500)
    diagnostic_test_order=models.CharField(max_length=500)
    assessment=models.CharField(max_length=500)
    treatement_plan=models.CharField(max_length=500)
    blood_transfusion=models.CharField(max_length=500)
    
    
    class Meta:
        db_table="round_note"

