from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
   user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
