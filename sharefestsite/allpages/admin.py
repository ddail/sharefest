from django.contrib import admin
from .models import Users, ContactModel

# Register your models here.
admin.site.register(ContactModel)
admin.site.register(Users)