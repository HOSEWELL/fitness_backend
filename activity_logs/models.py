from django.db import models
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    ACTIVITY_TYPES = [
        ("cardio", "Cardio"),
        ("strength", "Strength"),
        ("flexibility", "Flexibility"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(choices=ACTIVITY_TYPES, max_length=20)
    duration = models.PositiveIntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"
