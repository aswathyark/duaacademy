from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_num=models.IntegerField()
    gender=models.CharField(max_length=100)
    dob=models.DateField()
    course=models.CharField(max_length=100)
    address=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='pictures')
    aadhar=models.ImageField(upload_to='pictures')
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    fee=models.CharField(max_length=255)
    def __str__(self):
        return (self.name)
class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    def __str__(self):
        return '{}'.format(self.name)
