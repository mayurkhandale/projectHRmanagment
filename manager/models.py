from django.db import models

# Create your models here.
class New_reqModel(models.Model):
    opprtunity_code=models.IntegerField(primary_key=True)
    qualifucation=models.CharField(max_length=30)
    registratin_start_from=models.DateField()
    age_limit=models.IntegerField()
    last_day_apply=models.DateField()
    department_id=models.IntegerField(unique=True)
    no_of_position=models.IntegerField()
    description=models.CharField(max_length=100)
    resposibility=models.CharField(max_length=100)
    contact_no=models.IntegerField()
