from django.db import models

class opd_billingmodel(models.Model):
    uhid=models.CharField(max_length=500)
    dr_name=models.CharField(max_length=500)
    reffered_by=models.CharField(max_length=500)
    bill_code=models.CharField(max_length=500)
    bill_date=models.DateField(max_length=500)
    bill_time=models.TimeField(max_length=500)
    caste_type=models.CharField(max_length=500)
    charge_price_list=models.CharField(max_length=500)
    charge_group=models.CharField(max_length=500)
    charge_code=models.CharField(max_length=500)
    charge_name=models.CharField(max_length=500)
    quantity_or_duration=models.CharField(max_length=500)
    rate=models.CharField(max_length=500)
    discount_in_percentage=models.CharField(max_length=500)
    discount_amount=models.CharField(max_length=500)
    net_amount=models.CharField(max_length=500)
    
    class Meta:
        db_table="opd_billing"

