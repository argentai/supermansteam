from django.db import models
from django.contrib.auth import get_user_model
s = [
    ('Private','Private'),
    ('Public','Public')
]

class dospital(models.Model):
    region_kg = models.CharField(max_length=50)
    person_quantity = models.DecimalField(max_digits=100, decimal_places=0) #нужно поменять
    public_or_private = models.CharField(max_length=15, choices=s)
    okpo = models.CharField(max_length=1000, unique=True)

    # def __str__(self):
    #     return self.okpo

class medical_officer(models.Model):
    full_name = models.CharField(max_length=90)
    pincode_passport = models.IntegerField()
    age = models.DateTimeField()
    work_experience = models.TextField()
    phone_number = models.IntegerField()


