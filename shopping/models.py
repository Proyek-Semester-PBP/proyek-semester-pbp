from django.db import models
from django.conf import settings

# Create your models here.
class RecommendedItem(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=255, default="/static/shopping/items/placeholder_item.jpg")
    price = models.BigIntegerField()
    description = models.TextField()
    link = models.URLField()
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL)

class RecommendedVendor(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=255, default="/static/shopping/vendors/placeholder_vendor.jpg")
    description = models.TextField()
    link = models.URLField()