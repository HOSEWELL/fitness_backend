from django.db import models  # Ensure this import exists

class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.email
