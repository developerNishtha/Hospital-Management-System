from django.db import models

class homepagemodel(models.Model):
    uhid=models.CharField(max_length=500)
    registration_date=models.DateField()
    registration_time=models.TimeField()
    aadhar_number=models.CharField(max_length=12)
    prefix=models.CharField(max_length=500)
    first_name=models.CharField(max_length=500)
    middle_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500)
    birthday=models.DateField()
    gender=models.CharField(max_length=500)
    blood_group=models.CharField(max_length=500)
    marital_status=models.CharField(max_length=100)
    age=models.CharField(max_length=3)
    weight=models.CharField(max_length=3)
    height=models.CharField(max_length=3)
    occupation=models.CharField(max_length=100)
    email_id=models.CharField(max_length=250)
    contact_no=models.CharField(max_length=100)
    address_line_1=models.CharField(max_length=500)
    address_line_2=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    pincode=models.CharField(max_length=15)
    allerge_details=models.CharField(max_length=500)
    
    
    class Meta:
        db_table="homepage"

