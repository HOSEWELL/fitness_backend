from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

class ActivityLog(models.Model):
    ACTIVITY_TYPES = [
        ("cardio", "Cardio"),
        ("strength", "Strength"),
        ("steps", "Steps"),
        ("workout", "Workout"),
        ("flexibility", "Flexibility"),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    activity_type = models.CharField(choices=ACTIVITY_TYPES, max_length=20)
    duration = models.PositiveIntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"
