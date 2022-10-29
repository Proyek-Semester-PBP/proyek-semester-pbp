from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default = 0)
    name = models.CharField(max_length = 100, default =1, null=True)
    email = models.CharField(max_length=254, default =2, null=True)
    mobile = models.CharField(max_length = 20, default =3, null=True)
    github = models.CharField(max_length = 100, default =4, null=True)
    instagram = models.CharField(max_length = 100, default =5, null=True)
    twitter = models.CharField(max_length = 100, default =6, null=True)
    facebook = models.CharField(max_length = 100, default =7, null=True)