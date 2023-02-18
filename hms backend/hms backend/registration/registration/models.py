from django.db import models

class registration(models.Model):
    #prefix=models.CharField(max_length=6)
    firstname=models.CharField(max_length=50)
    middlename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    adhaarcardnumber=models.IntegerField()
    gender=models.CharField(max_length=1)
    bloodgroup=models.CharField(max_length=3)
    birthdate=models.DateField()
    maritalstatus=models.CharField(max_length=7)
    occupation=models.CharField(max_length=20)
    registrationdate=models.DateField()
    registrationtime=models.TimeField()
    age=models.IntegerField()
    weight=models.IntegerField()
    height=models.IntegerField()
    emailid=models.EmailField(max_length = 254)
    phonenumber=models.IntegerField()
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField()
    allergydetails=models.CharField(max_length=500)

    # secondary number
    # nationality
    # refferred by
    # city 
    # state 
    # country
    # prefferred language
    # patient category
    # relative name
    # relation
    # insurance
    class Meta:
        db_table="registration"
