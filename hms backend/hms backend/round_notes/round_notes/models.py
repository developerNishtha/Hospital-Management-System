from django.db import models

class round_notesmodel(models.Model):
    round_note_number=models.CharField(max_length=500)
    date_rn=models.DateField(max_length=500)
    time_rn=models.CharField(max_length=500)
    rmo_dr_name=models.TimeField(max_length=500)
    dr_name=models.TimeField(max_length=500)
    visit_type=models.CharField(max_length=500)
    symptoms=models.CharField(max_length=500)
    examination=models.CharField(max_length=500)
    nursing_advice=models.CharField(max_length=500)
    lab_test_order=models.CharField(max_length=500)
    diagnostic_test_order=models.CharField(max_length=500)
    assessment=models.CharField(max_length=500)
    treatement_plan=models.CharField(max_length=500)
    blood_transfusion=models.CharField(max_length=500)
    
    
    class Meta:
        db_table="round_notes"

