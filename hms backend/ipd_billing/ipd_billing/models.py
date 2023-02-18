from django.db import models

class ipd_billingmodel(models.Model):
    uhid=models.CharField(max_length=50)
    dr_name=models.CharField(max_length=50)
    reffered_by=models.CharField(max_length=50)
    bill_code=models.CharField(max_length=50)
    bill_date=models.DateField()
    bill_time=models.TimeField()
    caste_type=models.CharField(max_length=50)
    charge_price_list=models.CharField(max_length=50)
    charge_group=models.CharField(max_length=50)
    charge_code=models.CharField(max_length=50)
    charge_name=models.CharField(max_length=50)
    quantity_or_duration=models.CharField(max_length=50)
    rate=models.CharField(max_length=50)
    discount_in_percentage=models.IntegerField()
    discount_amount=models.IntegerField()
    net_amount=models.IntegerField()
    
    class Meta:
        db_table="ipd_billing"

