# Generated by Django 3.0.7 on 2023-06-06 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_branchoffice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BranchOffice',
            new_name='Office',
        ),
    ]
