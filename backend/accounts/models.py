from django.db import models

class User(models.Model):

    Id = models.AutoField(primary_key=True)
    UserId = models.CharField(max_length=100)
    NickName = models.CharField(max_length=100)
    Password = models .CharField(max_length=100)
