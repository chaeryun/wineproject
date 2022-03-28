from django.db import models

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