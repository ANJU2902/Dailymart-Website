from django.db import models
# Create your models here.
class categorydb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=False)
    description=models.CharField(max_length=100,null=True,blank=False)
    photo=models.ImageField(upload_to='image',null=True,blank=False)

class productdb(models.Model):
    pname=models.CharField(max_length=100,null=True,blank=False)
    category=models.CharField(max_length=100,null=True,blank=False)
    weight=models.IntegerField(null=True,blank=False)
    price=models.CharField(max_length=100,null=True,blank=False)
    photo=models.ImageField(upload_to='image',null=True,blank=False)

    