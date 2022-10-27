from django.db import models

# Create your models here.
class RecommendedItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.BigIntegerField()
    description = models.TextField()
    link = models.URLField()

class RecommendedVendor(models.Model):
    name = models.CharField(max_length=150)
    description = description = models.TextField()
    link = models.URLField()