from django.db import models
# from django.contrib.auth import get_user_model
region = [
    ('Bishkek', 'Bishkek'),
    ('Osh', 'Osh'),
    ('Naryn', 'Naryn')
]
hos = [
    ('Городская Клиническая больница №1', 'Bishkek'),
    ('Ошская городская клиническая больница', 'Osh'),
    ('Центр семейной медицины Нарынской области', 'Naryn'),
]

class Hospital(models.Model):
    name = models.CharField(max_length=100, choices=hos) #выбро больницы(называние больницы)
    region_kg = models.CharField(name, max_length=50, choices=region) #выбро региона(зависит от больницы)
    person_quantity = models.DecimalField(max_digits=100, decimal_places=0)
    public_or_private = models.BooleanField(default=False)
    okpo = models.CharField(max_length=1000, unique=True)

    def __str__(self):
        return self.name

class GlavVrach(models.Model):
    full_name = models.CharField("Ф.И.О Глав-Врача", max_length=90, blank=True, null=True)
    doctor = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    pincode_passport = models.DecimalField("Пинкод пасспорта", max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    work_experience = models.TextField("Опыт работы", blank=False)
    number = models.CharField("Номер телефона", max_length=10, blank=True, null=True)

    def __str__(self):
        return self.full_name

p = [
    ('Terapevt', 'Terapevt'),
    ('Hirurg', 'Hirurg')
]

class Lech_vrach(models.Model):
    full_name = models.CharField("Ф.И.О Врача", max_length=90, blank=True, null=True)
    napravlenie = models.TextField("Направление", max_length=300, blank=True, null=True)
    vybor = models.CharField(Hospital, "Выберите врача", max_length=100, choices=p, default='none')
    pincode_passport = models.DecimalField("Пинкод пасспорта", max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    work_experience = models.TextField("Опыт работы", blank=False)
    number = models.CharField("Номер телефона", max_length=10, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Medsestra(models.Model):
    full_name = models.CharField("Ф.И.О Медсестры", max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField("Пинкод пасспорта", max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    number = models.CharField("Номер телефона", max_length=10, blank=True, null=True)
    position = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Pacient(models.Model):
    full_name = models.CharField(max_length=90, blank=True, null=True)
    pincode_passport = models.DecimalField(max_digits=4, decimal_places=0, default="0000")
    age = models.IntegerField("Возраст", default=0)
    number = models.CharField("Номер телефона", max_length=10, blank=True, null=True)
    reason = models.TextField(blank=True)



