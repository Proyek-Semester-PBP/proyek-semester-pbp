from distutils.command.upload import upload
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default = 0)
    name = models.CharField(max_length = 100, default = 0, null=True)
    email = models.CharField(max_length=254, default = 0, null=True)
    mobile = models.CharField(max_length = 20, default = 0, null=True)
    github = models.CharField(max_length = 100, default = 0, null=True)
    instagram = models.CharField(max_length = 100, default = 0, null=True)
    twitter = models.CharField(max_length = 100, default = 0, null=True)
    facebook = models.CharField(max_length = 100, default = 0, null=True)
    point = models.BigIntegerField(default = 0)
    weight = models.BigIntegerField(default=0)
    profpic = models.ImageField(null = True, upload_to = 'pics/', blank = True, max_length = 500)
