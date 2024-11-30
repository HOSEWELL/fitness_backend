from django.urls import path
from .views import (
    ProfileListCreateView, ProfileDetailView,
    GoalListCreateView, GoalDetailView,
    FitnessStatsListCreateView, FitnessStatsDetailView,
    ActivityLogListCreateView, ActivityLogDetailView
)

urlpatterns = [
    # Profiles
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

    # Goals
    path('goals/', GoalListCreateView.as_view(), name='goal-list'),
    path('goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),

    # Fitness Stats
    path('fitness-stats/', FitnessStatsListCreateView.as_view(), name='fitness-stats-list'),
    path('fitness-stats/<int:pk>/', FitnessStatsDetailView.as_view(), name='fitness-stats-detail'),

    # Activity Logs
    path('activity-logs/', ActivityLogListCreateView.as_view(), name='activity-log-list'),
    path('activity-logs/<int:pk>/', ActivityLogDetailView.as_view(), name='activity-log-detail'),
]
