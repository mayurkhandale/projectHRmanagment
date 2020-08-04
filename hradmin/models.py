from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    empployee_id=models.IntegerField(primary_key=True)
    employee_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    disignation=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    contact_no=models.IntegerField(unique=True)
    email=models.EmailField()

