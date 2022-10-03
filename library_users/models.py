from distutils.command.upload import upload
from enum import unique
from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileinfo(models.Model):
    # To add more attrbuytes to the actual User we add user which inherit from User and add 
    # on it, because of that we create the following use er with one to one relation with the User built in opject
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    department = models.CharField(max_length=56,blank = True,unique=False)
    profile_image = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username 
        
