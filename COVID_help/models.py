from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50,default="")
    Locality = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=50,default="")
    name_suf = models.CharField(max_length=50,default="")
    name_phn = models.CharField(max_length=50,default="")

