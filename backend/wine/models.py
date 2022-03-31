from django.db.models.deletion import CASCADE
from django.db import models
from django.conf import settings
# Create your models here.

class Wine(models.Model):
    wine = models.CharField(max_length=500, primary_key=True)
    winery = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    image = models.URLField()
    color = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    light = models.FloatField()
    smooth = models.FloatField()
    dry = models.FloatField()
    soft = models.FloatField()
    gentle = models.FloatField()
    taste = models.TextField(null=True)
    food = models.TextField(null=True) 
    grapes = models.TextField(null=True) 
    alcohol = models.FloatField()

class Userlikewine(models.Model):
    wine = models.ForeignKey(Wine, on_delete=CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = models.DateField(auto_now=True)

class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    precip = models.FloatField()
    temp_max = models.FloatField()
    temp_min = models.FloatField()
    solar = models.FloatField()
    moist_max = models.FloatField()
    moist_min = models.FloatField()

