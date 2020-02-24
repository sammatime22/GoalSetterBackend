from rest_framework import serializers
from .models import User, Goal, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = {'user', 'name', 'tasks_completed', 'description', 'flat_goal'}

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = {'goal', 'time', 'completed', 'name', 'notes'}
