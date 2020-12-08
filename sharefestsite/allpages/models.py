from django.db import models
from multi_email_field.fields import MultiEmailField
from django.db.models import Model
from django.contrib.auth import get_user_model

class ContactModel(models.Model):
    emails = MultiEmailField()

class AllUser(models.Model):
    title = models.CharField(verbose_name='title',max_length=30,null=True,blank=True)
    emailList = []
    user = get_user_model()
    userList = user.objects.values_list('email')
    for i in userList:
        string = str(i)
        oldstr = string.replace('(','').replace(')','')
        newstr = oldstr.replace("'",'').replace(',',';')
        print(newstr)
        emailList.append(newstr)
    
    print(emailList)
            
    #alist = User.objects.all().values_list('email')

    def __str__(self):
        return self.title