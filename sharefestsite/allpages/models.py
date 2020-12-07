from django.db import models
from multi_email_field.fields import MultiEmailField
from django.db.models import Model

class ContactModel(models.Model):
    emails = MultiEmailField()

#class Person(models.Model):
#first_name = models.CharField(max_length=30)
class Users(models.Model):
    Email = models.CharField(verbose_name='Email',max_length=30,null=True,blank=True)
    Phone = models.CharField(verbose_name='Phone Number',max_length=10,null=True,blank=True)

    def __str__(self):
        return self.Email