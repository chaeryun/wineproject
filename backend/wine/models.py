from django.db.models.deletion import CASCADE
from django.db import models
from django.conf import settings
# Create your models here.

class Wine(models.Model):
    wine_id = models.IntegerField(primary_key=True)
    wine = models.CharField(max_length=500, default="Unknown_Wine")
    winery = models.CharField(max_length=500, default="Unknown_Winery")
    country = models.CharField(max_length=500, default="Unknown_Country")
    location = models.CharField(max_length=500, default="Unknown_Location")
    image = models.URLField(default="Cannot_found_ImageURL")
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    light = models.FloatField()
    smooth = models.FloatField()
    dry = models.FloatField()
    soft = models.FloatField()
    gentle = models.FloatField()
    taste = models.TextField(null=True)
    food = models.TextField(null=True) 
    grapes = models.TextField(null=True) 
    alcohol = models.FloatField()
    likes = models.IntegerField(default=0)

class Userlikewine(models.Model):
    wine = models.ForeignKey(Wine, on_delete=CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = models.DateField(auto_now=True)
