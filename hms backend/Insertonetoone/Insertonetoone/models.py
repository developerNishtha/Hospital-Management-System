from django.db import models    

class coursename(models.Model):
    cname=models.CharField(max_length=500)


class coursedetails(models.Model):
    course_details=models.CharField(max_length=500)
    level=models.CharField(max_length=500)
    duration=models.CharField(max_length=500)   
    fees=models.IntegerField()
    
    courses=models.OneToOneField(coursename,on_delete=models.CASCADE,related_name='courseobj')
    