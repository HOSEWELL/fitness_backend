from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    GOAL_TYPES = [
        ("steps", "Steps"),
        ("calories", "Calories"),
        ("workout", "Workout Duration"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_type = models.CharField(choices=GOAL_TYPES, max_length=20)
    goal_value = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default="Active")  # Active/Completed/Missed

    def __str__(self):
        return f"{self.user.username} - {self.goal_type}"
