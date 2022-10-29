from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class RecycleHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    weight = models.PositiveBigIntegerField()
    point = models.PositiveBigIntegerField()
    location = models.TextField()
    is_pickup = models.BooleanField(default=False)
    description = models.TextField(blank=True)

