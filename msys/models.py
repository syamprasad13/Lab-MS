'''from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


class InsertData(models.Model):
    Particulars   =models.CharField(max_length=25)
    Rollno   = models.PositiveIntegerField(max_length=10)
    Make   = models.CharField(max_length=25)
    SL No:  = models.PositiveIntegerFields(max_length=30)
    Quantity  = models.CharFmodels.CharField(max_length=25)
    Model No  = models.PositiveIntegerField(max_length=25)  
    Date     = models.CharField(max_length=20, default='date')
    Remarks = models.CharField(max_length=25)
   

    def __str__(self):
        return "%s" % (self.RollNo)


class DisplayData(models.Model):
    Particulars   =models.CharField(max_length=25)
    Rollno   = models.PositiveIntegerField(max_length=10)
    Make   = models.CharField(max_length=25)
    SL No:  = models.PositiveIntegerFields(max_length=30)
    Quantity  = models.CharFmodels.CharField(max_length=25)
    Model No  = models.PositiveIntegerField(max_length=25)  
    Date     = models.CharField(max_length=20, default='date')
    Remarks = models.CharField(max_length=25)
   

    def __str__(self):
        return "%s" % (self.RollNo)

class Login(models.Model):
    UserName   = models.CharField(max_length=25)
    Password   = models.CharField(max_length=25)

class Users(models.Model):

    def __str__(self):
        return "%s" % (self.UserName)
'''

#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

#class CustomUser(AbstractUser):
   # name = models.TextField(max_length=20)


    #def __str__(self):
     #    return self.username


# class Post(models.Model):

#     text = models.TextField()


class DataEntrycc1(models.Model):
    System_No  = models.CharField(max_length=20)
    Date        = models.CharField(max_length=20, default='date')
    Make        = models.TextField(max_length=50)
    Model_No    = models.TextField(max_length=50)
    Quantity    = models.IntegerField()
    Particulars = models.TextField(max_length=100)
    Remarks     = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Computer Lab 1"
    
    def get_absolute_url(self):
        return reverse("successcc1", kwargs={"pk": self.pk})

    def __str__(self):
         return "%s" %(self.System_No)


class DataEntrycc2(models.Model):
    System_No  = models.CharField(max_length=20)
    #Date = models.DateTimeField(auto_now_add=True)
    Date        = models.CharField(max_length=20, default='date')
    Make        = models.TextField(max_length=50)
    Model_No    = models.TextField(max_length=50)
    Quantity    = models.IntegerField()
    Particulars = models.TextField(max_length=100)
    Remarks     = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Computer Lab 2"
    
    def get_absolute_url(self):
        return reverse("successcc2", kwargs={"pk": self.pk})

    def __str__(self):
        return "%s " % (self.System_No)


class DataEntryacl(models.Model):
    System_No  = models.CharField(max_length=20)
    Date        = models.CharField(max_length=20, default='date')
    Make        = models.TextField(max_length=50)
    Model_No    = models.TextField(max_length=50)
    Quantity    = models.IntegerField()
    Particulars = models.TextField(max_length=100)
    Remarks     = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Advanced Computing Lab "
    
    def get_absolute_url(self):
        return reverse("successacl", kwargs={"pk": self.pk})

    def __str__(self):
        return "%s " % (self.System_No)

    


    
