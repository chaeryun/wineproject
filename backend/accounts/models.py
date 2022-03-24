from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
