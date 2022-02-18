# Generated by Django 4.0.2 on 2022-02-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlavVrach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=90)),
                ('pincode_passport', models.IntegerField()),
                ('age', models.DateTimeField()),
                ('work_experience', models.TextField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_kg', models.CharField(max_length=50)),
                ('person_quantity', models.DecimalField(decimal_places=0, max_digits=100)),
                ('public_or_private', models.CharField(choices=[('Private', 'Private'), ('Public', 'Public')], max_length=15)),
                ('okpo', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='medical_officer',
            new_name='lech_vrach',
        ),
        migrations.DeleteModel(
            name='dospital',
        ),
    ]
