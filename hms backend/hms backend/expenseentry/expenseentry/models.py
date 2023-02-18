from django.db import models

class expenseentrymodel(models.Model):
    entrycode=models.IntegerField()
    expensename=models.CharField(max_length=50)
    expensetype=models.CharField(max_length=50)
    preparedby=models.CharField(max_length=50)
    remarks=models.CharField(max_length=500)
    expenseamount=models.IntegerField()
    
    class Meta:
        db_table="expenseentry"

