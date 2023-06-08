from django.db import models
from . models import *
# Create your models here.
class User(models.Model):
    # Fields specific to the online store user
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.ForeignKey('Address', on_delete=models.CASCADE,related_name='users')
    profile_picture = models.ImageField(upload_to='profile_pictures')
    is_subscribed = models.BooleanField(default=False)
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
class Address(models.Model):
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.postal_code}, {self.country}"
    
# create user Account
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname