from django.db import models

# Create your models here.

class Wine(models.Model):
    Winery = models.CharField(max_length=500)
    Location = models.CharField(max_length=500)
    Image = models.URLField()
    Color = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Light = models.FloatField()
    Smooth = models.FloatField()
    Dry = models.FloatField()
    Soft = models.FloatField()
    Gentle = models.FloatField()
    Taste = models.TextField(null=True) #리스트 처리 X - 텍스트로 받아온 뒤 디코딩
    Food = models.TextField(null=True) #리스트 처리 X - 텍스트로 받아온 뒤 디코딩
    Grapes = models.TextField(null=True) #리스트 처리 X - 텍스트로 받아온 뒤 디코딩
    Alcohol = models.FloatField()

    
    