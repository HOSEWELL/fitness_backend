from django.db import models
from django.contrib.auth.models import User

class FitnessStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(unique_for_date="user")
    steps = models.PositiveIntegerField()
    calories_burned = models.FloatField()
    workout_duration = models.PositiveIntegerField()  # in minutes

    def __str__(self):
        return f"{self.user.username} - {self.date}"
