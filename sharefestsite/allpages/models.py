from django.db import models
from multi_email_field.fields import MultiEmailField

class ContactModel(models.Model):
    emails = MultiEmailField()

#class Person(models.Model):
#first_name = models.CharField(max_length=30)
