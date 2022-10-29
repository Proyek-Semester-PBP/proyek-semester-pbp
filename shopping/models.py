from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class RecommendedItem(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=255, default="/static/shopping/items/placeholder_item.jpg")
    price = models.BigIntegerField()
    description = models.TextField()
    link = models.URLField()

class RecommendedVendor(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=255, default="/static/shopping/vendors/placeholder_vendor.jpg")
    description = models.TextField()
    link = models.URLField()