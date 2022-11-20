from django.db import models

# Create your models here.
class takeNotes(models.Model):
    note = models.CharField(max_length=102)
    desc = models.CharField(max_length=100)
    important=models.CharField(max_length=3,default='off')

class contactUs(models.Model):
    name = models.CharField(max_length=100)
    phonenumber = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)
    issue = models.CharField(max_length=300)

class contactOrg(models.Model):
    phonenumber = models.IntegerField(max_length=10)
    email = models.EmailField(max_length=50)