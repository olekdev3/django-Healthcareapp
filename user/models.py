from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from simple_history.models import HistoricalRecords

# Create your models here.


class Patient(models.Model):
    uid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    dob=models.DateField()
    house=models.CharField(max_length=50)
    street=models.CharField(max_length=50)
    landmark=models.CharField(max_length=50)
    postoffice=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin_code=models.IntegerField()
    #details=models.ForeignKey(Details,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('dashboard')

class Details(models.Model):
    aadhar=models.IntegerField(primary_key=True)
    doctor=models.CharField(max_length=50)
    diagnosis=models.TextField()
    recommendation=models.TextField()
    medicine=models.TextField()
    test=models.TextField()
    history=HistoricalRecords()

    def get_absolute_url(self):
        return reverse('dashboard')

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=20)
    dob=models.DateField()
    Gender=models.CharField(max_length=10)
    bloodGroup=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} profile'




    
