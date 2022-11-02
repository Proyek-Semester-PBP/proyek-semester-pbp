from contextlib import nullcontext
from re import T
from django.db import models
from django.contrib.auth.models import User

class RecycleHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    name = models.CharField(default="", max_length=250, null = True)
    date = models.DateTimeField(auto_now=True, null = True)
    weight = models.PositiveBigIntegerField(default = 0)
    point = models.PositiveBigIntegerField(default = 0)
    location = models.TextField(null = True)
    is_pickup = models.BooleanField(default=False, null = True)
    description = models.TextField(blank=True, null = True)

# Create your models here.
