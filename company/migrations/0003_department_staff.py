# Generated by Django 3.0.7 on 2023-06-06 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_selladdress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeID', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=3)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('officeNo', models.CharField(max_length=100)),
                ('floorNo', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
            ],
        ),
    ]
