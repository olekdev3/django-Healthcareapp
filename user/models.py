from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from simple_history.models import HistoricalRecords

# Create your models here.


class Patient(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.TextField()
    gender=models.TextField()
    dob=models.TextField()
    house=models.TextField()
    street=models.TextField()
    landmark=models.TextField()
    postoffice=models.TextField()
    district=models.TextField()
    state=models.TextField()
    pin_code=models.IntegerField()
    #details=models.ForeignKey(Details,on_delete=models.CASCADE)

class Details(models.Model):
    aadhar=models.IntegerField(primary_key=True)
    doctor=models.TextField()
    diagnosis=models.TextField()
    recommendation=models.TextField()
    medicine=models.TextField()
    test=models.TextField()
    history=HistoricalRecords()







    
