from django.db import models
# from django.contrib.auth import get_user_model
region = [
    ('Bishkek','Bishkek'),
    ('Osh','Osh'),
    ('Naryn','Naryn')
]

class Hospital(models.Model):
    region_kg = models.CharField(max_length=50, choices=region)
    person_quantity = models.DecimalField(max_digits=100, decimal_places=0) #нужно поменять
    public_or_private = models.BooleanField(default=False)
    okpo = models.CharField(max_length=1000, unique=True)

class GlavVrach(models.Model):
    full_name = models.CharField(max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField(max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    work_experience = models.TextField(blank=False)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

p = [
    ('Terapevt','Terapevt'),
    ('Hirurg','Hirurg')
]

class Lech_vrach(models.Model):
    napravlenie = models.CharField(max_length=200, blank=True, null=True)
    vybor = models.CharField(max_length=100, choices=p, default='none')
    full_name = models.CharField(max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField(max_digits=4, decimal_places=0,default="0000")
    age = models.IntegerField("Возраст", default=0)
    work_experience = models.TextField(blank=False)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

class Medsestra(models.Model):
    full_name = models.CharField(max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField(max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

class Pacient(models.Model):
    full_name = models.CharField(max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField(max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    reason = models.TextField(blank=True)


