from django.db import models


# Create your models here.
class User(models.Model):
    phoneNum=models.BigIntegerField(primary_key=True)
    userName=models.CharField(max_length=10)
    passWrod=models.CharField(max_length=16)
    credit = models.CharField(max_length=3,default="8")

class Phone(models.Model):
    phoneId = models.IntegerField(primary_key=True)
    phoneMode = models.CharField(max_length=40)
    phoneDetail = models.CharField(max_length=100)
    phonePrice = models.IntegerField()
    area = models.CharField(max_length=10)
    phoneImgUrl = models.CharField(max_length=150)
    phoneGrade = models.CharField(max_length=3,default="9")
    manufacturer =models.CharField(max_length=8,default="")

class College(models.Model):
    collegeId = models.BigIntegerField(primary_key=True)
    collegeName = models.CharField(max_length=16)
    collegeArea = models.CharField(max_length=10)
    collegeGrade = models.CharField(max_length=2)

class Commodity(models.Model):
    phonenum = models.IntegerField(primary_key=True,)
    phoneModel = models.CharField(max_length=5,null=True)
    phonePrice = models.CharField(max_length=15,null=True)
    phoneCharacter = models.CharField(max_length=10,null=True)

class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()

class Order(models.Model):
    no = models.CharField(max_length=64)
    goods = models.ForeignKey(to='Goods',on_delete=models.CASCADE)
    status_choices = (
        (1,'未支付'),
        (2,'已支付'),
    )
    status = models.IntegerField(choices=status_choices,default=1)
