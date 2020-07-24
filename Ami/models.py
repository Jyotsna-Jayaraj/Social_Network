from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=999)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return name