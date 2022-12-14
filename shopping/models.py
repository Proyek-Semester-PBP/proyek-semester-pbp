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

    def __str__(self):
        return self.name

class RecommendedVendor(models.Model):
    name = models.CharField(max_length=150)
    image = models.CharField(max_length=255, default="/static/shopping/vendors/placeholder_vendor.jpg")
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name

class Review(models.Model):
    item = models.CharField(max_length=150)
    user = models.CharField(max_length=150)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.item + ", " + self.user