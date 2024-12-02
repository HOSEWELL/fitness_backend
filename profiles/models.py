from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


