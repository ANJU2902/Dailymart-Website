from django.db import models

from dailymartapp.models import productdb
from django.db.models.deletion import CASCADE


# Create your models here.
class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    email=models.EmailField(null=True,blank=False)
    subject=models.CharField(max_length=100,null=True,blank=False)
    message=models.CharField(max_length=100,null=True,blank=False)

class registerdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    email=models.EmailField(null=True,blank=False)
    phone=models.IntegerField(null=True,blank=False)
    username=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=100,null=True,blank=False)
    
class cartdb(models.Model):
    productid = models.ForeignKey(productdb,on_delete=CASCADE,null=True,blank=True)
    userid = models.ForeignKey(registerdb,on_delete=CASCADE,null=True,blank=False)
    total = models.IntegerField(null=True,blank=False)
    quantity = models.IntegerField(null=True,blank=False)
    status = models.IntegerField(null=True,blank=False)

class checkoutdb(models.Model):
    cartid = models.ForeignKey(cartdb,on_delete=CASCADE,null=True,blank=False)
    name = models.CharField(max_length=200,null=True,blank=False)
    email = models.EmailField(null=True,blank=False)
    mobile = models.IntegerField(blank=False,null=True)
    address = models.TextField(max_length=200,null=True,blank=False)
