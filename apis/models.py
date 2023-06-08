from django.db import models

# Create your models here.

class ApisModel(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    descr = models.CharField(max_length = 200)
 
    def __str__(self):
        return self.title
    

class V1Model(models.Model):
    firstname    = models.CharField(max_length = 200)
    lastname    = models.CharField(max_length = 200)
    sex         = models.CharField(max_length = 200)
    region      = models.CharField(max_length = 200)
    yearof      = models.CharField(max_length = 200)
    age      = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.firstname
    
    