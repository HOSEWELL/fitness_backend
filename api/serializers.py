from django.contrib.auth.models import User
from rest_framework import serializers
from profiles.models import Profile
from fitness_stats.models import FitnessStats
from goals.models import Goal
from activity_logs.models import ActivityLog

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'email', 'password', 'age', 'weight', 'height', 'profile_image']



class FitnessStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessStats
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'


class ActivityLogSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())  # Updated to Profile

    class Meta:
        model = ActivityLog
        fields = '__all__'

