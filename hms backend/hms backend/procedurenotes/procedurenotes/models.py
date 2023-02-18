from django.db import models

class procedurenotesmodel(models.Model):
    procedure_date=models.DateField()
    procedure_name=models.CharField(max_length=500)
    ot_name=models.CharField(max_length=500)
    procedure_time=models.TimeField()
    in_time=models.TimeField()
    out_time=models.TimeField()
    surgeon_name=models.CharField(max_length=500)
    assistant_surgeon_1=models.CharField(max_length=500)
    assistant_surgeon_2=models.CharField(max_length=500)
    anastheiologist=models.CharField(max_length=500)
    procedure_type=models.CharField(max_length=500)
    symoptom_of_infection=models.CharField(max_length=500)
    culture_report=models.CharField(max_length=500)
    operation_status=models.CharField(max_length=500)
    risk_factors=models.CharField(max_length=500)
    anasthesia_notes=models.CharField(max_length=500)
    pre_operative_notes=models.CharField(max_length=500)
    post_operative_notes=models.CharField(max_length=500)
    procedure_notes=models.CharField(max_length=500)
    remarks=models.CharField(max_length=500)
    
    class Meta:
        db_table="procedurenotes"

