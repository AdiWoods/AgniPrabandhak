from django.db import models
# Create your models here.

# image location date and time   phone no
# long lattitude from the location 

class ReportData(models.Model):
    longitude=models.CharField(max_length=30,null=False)
    lattitude=models.CharField(max_length=30,null=False)
    fireimage=models.FileField(upload_to='fireimage/')
    date=models.CharField(max_length=30,null=True)
    


    
    

# forest department data
class ForestDepartmentData(models.Model):
    location = models.CharField(max_length=50 , null= False )
    phone_no=models.CharField(max_length=20,null=False,unique=True)
    longitude=models.CharField(max_length=20,null=True,unique=True)
    lattitude=models.CharField(max_length=20,null=True,unique=True)
    
    

    
    
    
    # fireimage=models.FileField(upload_to='fireimage/',null=True,default=None)


