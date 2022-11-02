from django.db import models

# Create your models here.

class NewsData(models.Model):
    title = models.TextField(max_length=50)
    date = models.CharField(max_length=30)
