from django.db import models
from datetime import datetime

# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class SellAddress(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    # reg_date = models.date()
    # update_date = models.date()
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.fname
class Department(models.Model):
    deptName = models.CharField(max_length=100)

    def __str__(self):
        return self.deptName
class Attendance(models.Model):
    # Subject Attendance
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    def __str__(self):
        return self.attendance_date
class Staff(models.Model):
    employeeID = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=100)
    department = models.CharField
    phone_number = models.CharField(max_length=100)
    officeNo = models.CharField(max_length=100)
    floorNo = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeID
class Feedback(models.Model):
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.CharField(max_length=3)
    email = models.CharField(max_length=100)
    department = models.CharField
    phone_number = models.CharField(max_length=100)
    
    def __str__(self):
        return self.full_name
    
class Office(models.Model):
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=10)
    zone = models.CharField(max_length=3)
    address = models.CharField(max_length=100)
    email = models.CharField
    phone_number = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region