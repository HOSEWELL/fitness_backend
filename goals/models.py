from django.db import models
from profiles.models import Profile

class Goal(models.Model):
    GOAL_TYPES = [
        ("cardio", "Cardio"),
        ("strength", "Strength"),
        ("steps", "Steps"),
        ("workout", "Workout"),
        ("flexibility", "Flexibility"),
    ]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    goal_type = models.CharField(choices=GOAL_TYPES, max_length=20)
    goal_value = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default="Active")  

    def __str__(self):
        return f"{self.user.email} - {self.goal_type}"
