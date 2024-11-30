from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from profiles.models import Profile
from goals.models import Goal
from fitness_stats.models import FitnessStats
from activity_logs.models import ActivityLog
from .serializers import ProfileSerializer, GoalSerializer, FitnessStatsSerializer, ActivityLogSerializer
from django.contrib.auth.models import User



# Profile Views
class ProfileListCreateView(APIView):
    # GET: Retrieve all profiles
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    # POST: Create a new profile
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailView(APIView):
    # GET: Retrieve a specific profile by ID
    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # PUT: Update a specific profile
    def put(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a specific profile
    def delete(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Goal Views
class GoalListCreateView(APIView):
    # GET: Retrieve all goals
    def get(self, request):
        goals = Goal.objects.all()
        serializer = GoalSerializer(goals, many=True)
        return Response(serializer.data)

    # POST: Create a new goal
    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoalDetailView(APIView):
    # GET: Retrieve a specific goal by ID
    def get(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

    # PUT: Update a specific goal
    def put(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Delete a specific goal
    def delete(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Repeat similar structure for FitnessStats and ActivityLog
class FitnessStatsListCreateView(APIView):
    def get(self, request):
        stats = FitnessStats.objects.all()
        serializer = FitnessStatsSerializer(stats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FitnessStatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FitnessStatsDetailView(APIView):
    def get(self, request, pk):
        stats = get_object_or_404(FitnessStats, pk=pk)
        serializer = FitnessStatsSerializer(stats)
        return Response(serializer.data)

    def put(self, request, pk):
        stats = get_object_or_404(FitnessStats, pk=pk)
        serializer = FitnessStatsSerializer(stats, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stats = get_object_or_404(FitnessStats, pk=pk)
        stats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActivityLogListCreateView(APIView):
    def get(self, request):
        logs = ActivityLog.objects.all()
        serializer = ActivityLogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivityLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityLogDetailView(APIView):
    def get(self, request, pk):
        log = get_object_or_404(ActivityLog, pk=pk)
        serializer = ActivityLogSerializer(log)
        return Response(serializer.data)

    def put(self, request, pk):
        log = get_object_or_404(ActivityLog, pk=pk)
        serializer = ActivityLogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        log = get_object_or_404(ActivityLog, pk=pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
