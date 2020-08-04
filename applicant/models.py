from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    name=models.CharField(max_length=30)
    date_of_birth=models.DateField()
    email_id=models.EmailField(unique=True)
    gender=models.CharField(max_length=10)
    mobaile_no=models.IntegerField()
    address=models.CharField(max_length=100)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)

class ApplicationformModel(models.Model):
    name=models.CharField(max_length=30)
    Date_of_birth=models.DateField()
    emailid=models.EmailField(unique=True)
    gender=models.CharField(max_length=10)
    phone_no=models.IntegerField()
    address=models.CharField(max_length=100)
    qualification=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    percentage=models.FloatField()
    upload_resume=models.FileField(upload_to="applicationresumes/")




